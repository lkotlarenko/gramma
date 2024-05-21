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

class ClipboardListener:
    def __init__(self):
        self.load_env_vars()
        self.last_called = 0
        self.client = AsyncGroq(api_key=self.GROQ_API_KEY)
        self.commands = self.load_commands()

    def load_env_vars(self) -> None:
        load_dotenv()
        self.GROQ_API_KEY = os.getenv('GROQ_API_KEY')

    def load_commands(self) -> Dict[str, str]:
        return {key: value for key, value in os.environ.items() if key.startswith('PROMPT_')}

    async def process_command(self, command: str, user_msg: str) -> None:
        if time.time() - self.last_called < 4:
            notification.notify(
                title="Rate Limit",
                message="Please wait a few seconds before trying again.",
                app_name="Gramma",
                timeout=3
            )
            return

        prompt = self.commands.get(f'PROMPT_{command.upper()}')
        if not prompt:
            return

        try:
            completion = await self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": user_msg}
                ],
                model="llama3-70b-8192",
                temperature=0.5,
                max_tokens=1024,
                top_p=1,
                stop=None,
                stream=False,
            )

            response_msg = completion.choices[0].message.content
            pyperclip.copy(response_msg)
            notification.notify(
                title="Processed",
                message="Text processed and copied to clipboard.",
                app_name="Gramma",
                timeout=3
            )
            self.last_called = time.time()
        except Exception as e:
            notification.notify(
                title="Error",
                message=f"An error occurred: {e}",
                app_name="Gramma",
                timeout=3
            )

    def process_command_sync(self, command: str, user_msg: str) -> None:
        asyncio.run(self.process_command(command, user_msg))

    def monitor_clipboard(self) -> None:
        recent_value = pyperclip.paste()
        while True:
            time.sleep(0.1)
            tmp_value = pyperclip.paste()
            if tmp_value != recent_value:
                recent_value = tmp_value
                for prefix in self.commands:
                    if tmp_value.startswith(f'!{prefix.lower()[7:]}'):
                        command = tmp_value.split(' ')[0][1:]
                        user_msg = tmp_value[len(command) + 2:].strip()  # +2 to account for space and '!'
                        self.process_command_sync(command, user_msg)

    def setup_tray_icon(self) -> None:
        icon_path = "src/images/tray_icon.png"
        image = Image.open(icon_path)
        icon = pystray.Icon("GrammarCorrector", image, "Grammar Corrector", menu=pystray.Menu(item('Exit', self.exit_program)))
        icon.run()

    def exit_program(self, icon) -> None:
        icon.stop()
        os._exit(0)

if __name__ == "__main__":
    listener = ClipboardListener()
    threading.Thread(target=listener.setup_tray_icon).start()
    listener.monitor_clipboard()
