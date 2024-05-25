import os
import json
from typing import Dict

COMMANDS_FILE = "commands.json"
SETTINGS_FILE = "settings.json"


class DataManager:
    def load_commands(self) -> Dict[str, str]:
        if os.path.exists(COMMANDS_FILE):
            with open(COMMANDS_FILE, "r") as file:
                return json.load(file)
        else:
            return {}

    def save_commands(self, commands: Dict[str, str]) -> None:
        with open(COMMANDS_FILE, "w") as file:
            json.dump(commands, file, indent=4)

    def load_settings(self) -> Dict[str, str]:
        if os.path.exists(SETTINGS_FILE):
            with open(SETTINGS_FILE, "r") as file:
                return json.load(file)
        else:
            return {"GROQ_API_KEY": "", "GROQ_MODEL": ""}

    def save_settings(self, settings: Dict[str, str]) -> None:
        with open(SETTINGS_FILE, "w") as file:
            json.dump(settings, file, indent=4)
