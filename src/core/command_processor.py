import pyperclip
import re
from groq import AsyncGroq

from src.data import SharedData
from src.utils import notify
from src.config import NOTIFICATION_TIMEOUT_SHORT, NOTIFICATION_TIMEOUT_LONG


class CommandProcessor:
    def __init__(self, shared_data: SharedData):
        self.shared_data = shared_data
        self.settings = self.shared_data.settings
        self.groq_model = str(self.settings.get("GROQ_MODEL"))
        self.api_key = str(self.settings.get("GROQ_API_KEY"))
        self.client = AsyncGroq(api_key=self.api_key)

    async def process_command(self, command: str, user_msg: str) -> None:
        prompt = self.shared_data.commands.get(command.upper())
        if not prompt:
            return

        try:
            completion = await self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": user_msg},
                ],
                model=self.groq_model,
                temperature=0.5,
                max_tokens=1024,
                top_p=1,
                stop=None,
                stream=False,
            )
            response_msg = completion.choices[0].message.content
            pyperclip.copy(response_msg)
            notify(
                "Gramma",
                f"Text processed using {self.groq_model} was copied to clipboard!",
                NOTIFICATION_TIMEOUT_SHORT,
            )
        except Exception as e:
            self.handle_error(str(e))

    def handle_error(self, error: str) -> None:
        error_message = self.extract_error_message(error)
        notify(
            "Gramma",
            f"An error occurred: {error_message}",
            NOTIFICATION_TIMEOUT_LONG,
        )

    def extract_error_message(self, error: str) -> str:
        match = re.search(r"'message': '([^']+)'", error)
        if match:
            return match.group(1)
        print(error)
        return "Unknown Error!"

    def update_data(self, shared_data: SharedData):
        self.shared_data = shared_data
        self.settings = shared_data.settings
        self.groq_model = str(self.settings.get("GROQ_MODEL"))
        self.api_key = str(self.settings.get("GROQ_API_KEY"))
        self.client = AsyncGroq(api_key=self.api_key)
