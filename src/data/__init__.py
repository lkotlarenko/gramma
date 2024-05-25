from typing import Dict
from .data_manager import DataManager


class SharedData:
    def __init__(self):
        self.data_manager = DataManager()
        self.commands = self.data_manager.load_commands()
        self.settings = self.data_manager.load_settings()

    def update_commands(self, new_commands: Dict[str, str]) -> None:
        self.commands = new_commands
        self.data_manager.save_commands(new_commands)

    def update_settings(self, new_settings: Dict[str, str]) -> None:
        self.settings = new_settings
        self.data_manager.save_settings(new_settings)

    def refresh_settings(self) -> None:
        self.settings = self.data_manager.load_settings()
