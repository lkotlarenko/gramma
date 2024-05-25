import customtkinter as ctk
from src.gui.base_page import BasePage
from tkinter import messagebox
from src.data import SharedData
from src.core.clipboard_listener import ClipboardListener


class SetupPage(BasePage):
    def __init__(self, shared_data: SharedData, listener: ClipboardListener):
        super().__init__(shared_data)
        self.listener = listener
        self.title("Setup")
        self.load_settings()

    def create_ui(self):

        self.api_key_label = ctk.CTkLabel(self, text="API Key:")
        self.api_key_label.pack(pady=10)
        self.api_key_entry = ctk.CTkEntry(self)
        self.api_key_entry.pack(pady=10, ipadx=150)
        self.model_label = ctk.CTkLabel(self, text="Groq model:")
        self.model_label.pack(pady=10)
        self.model_entry = ctk.CTkEntry(self)
        self.model_entry.pack(pady=10)

        self.save_button = ctk.CTkButton(
            self,
            text="Save",
            fg_color="green",
            hover_color="#66FF66",
            command=self.save_settings,
        )
        self.save_button.pack(pady=10)

    def load_settings(self):
        settings = self.shared_data.settings
        self.api_key_entry.delete(0, "end")
        self.api_key_entry.insert(0, settings.get("GROQ_API_KEY", ""))
        self.model_entry.delete(0, "end")
        self.model_entry.insert(0, settings.get("GROQ_MODEL", ""))

    def save_settings(self):
        if self.validate_input() and self.show_confirmation_dialog(
            "Save Settings", "Are you sure you want to save the changes?"
        ):
            new_settings = {
                "GROQ_API_KEY": self.api_key_entry.get(),
                "GROQ_MODEL": self.model_entry.get(),
            }
            self.shared_data.update_settings(new_settings)
            self.listener.refresh_data()
            self.destroy()

    def validate_input(self):
        api_key = self.api_key_entry.get()
        model = self.model_entry.get()

        if not api_key or not model:
            messagebox.showerror(
                "Invalid Input", "Please enter both API Key and Model."
            )
            return False

        return True
