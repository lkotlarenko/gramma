import os
import time
import asyncio
import pyperclip
from dotenv import load_dotenv
from groq import AsyncGroq
import pystray
from pystray import MenuItem as item
from PIL import Image
from plyer import notification
import threading
from typing import Dict
from commands import commands
import sys
from src.config import (
    APP_NAME,
    APP_ICON,
    TRAY_ICON,
    NOTIFICATION_TIMEOUT_SHORT,
    NOTIFICATION_TIMEOUT_LONG,
)

if sys.platform.startswith("win"):
    import win32event
    import win32api
    import winerror
else:
    import fcntl


class ClipboardListener:
    def __init__(self):
        self.load_env_vars()
        self.last_called = 0
        self.client = AsyncGroq(api_key=self.GROQ_API_KEY)
        self.commands = self.load_commands()
        self.ensure_single_instance()

    def load_env_vars(self) -> None:
        load_dotenv()
        self.GROQ_API_KEY = os.getenv("GROQ_API_KEY")
        self.GROQ_MODEL = os.getenv("GROQ_MODEL")

    def load_commands(self) -> Dict[str, str]:
        notification.notify(
            title=APP_NAME,
            message="Gramma is now running in the background!",
            app_name=APP_NAME,
            app_icon=APP_ICON,
            timeout=NOTIFICATION_TIMEOUT_LONG,
        )
        return commands

    async def process_command(self, command: str, user_msg: str) -> None:
        if time.time() - self.last_called < 4:
            self.notify(
                "Rate Limit",
                "Please wait a few seconds before trying again.",
                NOTIFICATION_TIMEOUT_LONG,
            )
            return

        prompt = self.commands.get(f"PROMPT_{command.upper()}")
        if not prompt:
            return

        try:
            completion = await self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": user_msg},
                ],
                model=self.GROQ_MODEL,
                temperature=0.5,
                max_tokens=1024,
                top_p=1,
                stop=None,
                stream=False,
            )

            response_msg = completion.choices[0].message.content
            pyperclip.copy(response_msg)
            self.notify(
                "Done!",
                "Text processed and copied to clipboard.",
                NOTIFICATION_TIMEOUT_SHORT,
            )
            self.last_called = time.time()
        except Exception as e:
            self.notify("Error", f"An error occurred: {e}", NOTIFICATION_TIMEOUT_LONG)

    def process_command_sync(self, command: str, user_msg: str) -> None:
        asyncio.run(self.process_command(command, user_msg))

    def notify(self, title: str, message: str, timeout: int) -> None:
        notification.notify(
            title=title,
            message=message,
            app_name=APP_NAME,
            app_icon=APP_ICON,
            timeout=timeout,
        )

    def monitor_clipboard(self) -> None:
        recent_value = pyperclip.paste()
        while True:
            time.sleep(0.1)
            tmp_value = pyperclip.paste()
            if tmp_value != recent_value:
                recent_value = tmp_value
                for prefix in self.commands:
                    if tmp_value.startswith(f"!{prefix.lower()[7:]}"):
                        command = tmp_value.split(" ")[0][1:]
                        user_msg = tmp_value[len(command) + 2 :].strip()
                        self.process_command_sync(command, user_msg)

    def setup_tray_icon(self) -> None:
        image = Image.open(TRAY_ICON)
        icon = pystray.Icon(
            APP_NAME,
            image,
            APP_NAME,
            menu=pystray.Menu(item("Exit", self.exit_program)),
        )
        icon.run()

    def exit_program(self, icon) -> None:
        icon.stop()
        os._exit(0)

    def ensure_single_instance(self) -> None:
        if sys.platform.startswith("win"):
            self.handle_mutex()
        else:
            self.handle_lock_file()

    def handle_mutex(self) -> None:
        self.mutex = None
        try:
            self.mutex = win32event.CreateMutex(None, False, APP_NAME)
            if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
                self.notify_instance_already_running()
        except Exception as e:
            print(f"Error creating mutex: {e}")
            os._exit(1)

    def handle_lock_file(self) -> None:
        lock_file = "/tmp/clipboardlistener.lock"
        try:
            self.lock_fd = os.open(lock_file, os.O_CREAT | os.O_EXCL | os.O_RDWR)
        except OSError:
            self.notify_instance_already_running()
            os._exit(1)
        else:
            fcntl.flock(self.lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)


if __name__ == "__main__":
    listener = ClipboardListener()
    threading.Thread(target=listener.setup_tray_icon).start()
    listener.monitor_clipboard()

    if sys.platform.startswith("win"):
        win32event.ReleaseMutex(listener.mutex)
    else:
        os.close(listener.lock_fd)
        os.unlink("/tmp/clipboardlistener.lock")
