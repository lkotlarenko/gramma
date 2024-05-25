import time
import threading
import pyperclip
import asyncio

from src.data import SharedData
from src.core.command_processor import CommandProcessor
from src.utils import notify
from src.config import NOTIFICATION_TIMEOUT_LONG


class ClipboardListener:
    def __init__(self, shared_data: SharedData):
        self.shared_data = shared_data
        self.command_processor = CommandProcessor(self.shared_data)
        self.monitoring_thread = threading.Thread(target=self.monitor_clipboard)
        self.monitoring_thread.start()
        notify(
            title="Gramma",
            message="Gramma is now running in the background!",
            timeout=NOTIFICATION_TIMEOUT_LONG,
        )

    def monitor_clipboard(self):
        recent_value = pyperclip.paste()
        while True:
            time.sleep(0.1)
            tmp_value = pyperclip.paste()
            if tmp_value != recent_value:
                recent_value = tmp_value
                self.process_command(tmp_value)

    def process_command(self, clipboard_text: str):
        if clipboard_text.startswith("!") and len(clipboard_text) > 2:
            command = clipboard_text[1:3].upper()
            user_msg = clipboard_text[3:].strip()
            asyncio.run(self.command_processor.process_command(command, user_msg))

    def stop_monitoring(self):
        self.monitoring_thread.join()

    def refresh_data(self):
        self.command_processor.update_data(self.shared_data)
        self.shared_data.refresh_settings()
