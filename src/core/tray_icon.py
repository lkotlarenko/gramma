import os
import threading
import pystray
from pystray import MenuItem as item
from PIL import Image

from src.config import APP_NAME, TRAY_ICON
from src.gui.setup_page import SetupPage
from src.gui.edit_commands_page import EditCommandsPage


class TrayIcon:
    def __init__(self, listener):
        self.listener = listener
        self.setup_tray_icon()

    def setup_tray_icon(self):
        try:
            image = Image.open(TRAY_ICON)
        except Exception as e:
            print(f"Error loading tray icon: {e}")
            return

        menu_items = [
            item("Setup", self.open_setup),
            item("Edit Commands", self.open_edit_commands, default=True),
            item("Exit", self.exit_program),
        ]

        menu = pystray.Menu(*menu_items)
        icon = pystray.Icon(APP_NAME, image, APP_NAME, menu=menu)

        icon.run()

    def open_setup(self):
        threading.Thread(target=self.run_setup_page).start()

    def open_edit_commands(self):
        threading.Thread(target=self.run_edit_commands_page).start()

    def run_setup_page(self):
        app = SetupPage(self.listener.shared_data, self.listener)
        app.mainloop()

    def run_edit_commands_page(self):
        app = EditCommandsPage(self.listener.shared_data)
        app.mainloop()

    def exit_program(self, icon):
        icon.stop()
        os._exit(0)
