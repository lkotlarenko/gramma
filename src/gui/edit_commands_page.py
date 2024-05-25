import customtkinter as ctk
from src.gui.base_page import BasePage
from tkinter import messagebox
from src.data import SharedData


class EditCommandsPage(BasePage):
    def __init__(self, shared_data: SharedData):
        super().__init__(shared_data)
        self.title("Edit Commands")
        self.geometry("800x600")
        self.load_commands()

    def create_ui(self):
        self.header_frame = ctk.CTkFrame(self)
        self.header_frame.pack(fill="x", pady=10)
        self.prefix_label = ctk.CTkLabel(
            self.header_frame, text="Prefix", width=100, anchor="center"
        )
        self.prefix_label.grid(row=0, column=0, padx=5)
        self.prompt_label = ctk.CTkLabel(
            self.header_frame, text="Prompt", width=600, anchor="center"
        )
        self.prompt_label.grid(row=0, column=1, padx=5)
        self.commands_frame = ctk.CTkFrame(self)
        self.commands_frame.pack(fill="both", expand=True, pady=10)

        self.save_button = ctk.CTkButton(
            self,
            text="Save",
            command=self.save_commands,
            fg_color="green",
            hover_color="#66FF66",
        )
        self.save_button.pack(pady=20)

        self.add_command_button = ctk.CTkButton(
            self,
            text="Add Command",
            command=self.add_command,
            fg_color="blue",
            hover_color="#6699FF",
        )
        self.add_command_button.pack(pady=10)

    def load_commands(self):
        self.entries = []
        commands = self.shared_data.commands
        for idx, (prefix, prompt) in enumerate(commands.items()):
            self.add_command_entry(idx, prefix, prompt)

    def add_command_entry(self, idx, prefix, prompt):
        prefix_entry = ctk.CTkEntry(self.commands_frame, width=100)
        prefix_entry.insert(0, prefix)
        prefix_entry.grid(row=idx, column=0, padx=10, pady=2, sticky="ew")
        prompt_entry = ctk.CTkEntry(self.commands_frame, width=600)
        prompt_entry.insert(0, prompt)
        prompt_entry.grid(row=idx, column=1, padx=10, pady=2, sticky="ew")

        delete_button = ctk.CTkButton(
            self.commands_frame,
            text="X",
            width=50,
            command=lambda idx=idx: self.delete_command(idx),
            fg_color="red",
            hover_color="#FF6666",
        )
        delete_button.grid(row=idx, column=2, padx=5, pady=2)
        self.entries.append((prefix_entry, prompt_entry, delete_button))

    def save_commands(self):
        if self.validate_input() and self.show_confirmation_dialog(
            "Save Commands", "Are you sure you want to save the changes?"
        ):
            new_commands = {
                f"{entry[0].get().upper()}": entry[1].get() for entry in self.entries
            }
            self.shared_data.update_commands(new_commands)
            self.destroy()

    def add_command(self):
        idx = len(self.entries)
        self.add_command_entry(idx, "", "")

    def delete_command(self, idx):
        if self.show_confirmation_dialog(
            "Delete Command", "Are you sure you want to delete this command?"
        ):
            for widget in self.entries[idx]:
                widget.destroy()
            self.entries.pop(idx)
            self.update_command_buttons()

    def update_command_buttons(self):
        for idx, (_, _, delete_button) in enumerate(self.entries):
            delete_button.configure(command=lambda idx=idx: self.delete_command(idx))

    def validate_input(self):
        used_prefixes = []
        for prefix_entry, prompt_entry, _ in self.entries:
            prefix = prefix_entry.get()
            prompt = prompt_entry.get()
            if not prompt:
                messagebox.showerror("Invalid command", "Prompts cannot be empty.")
                return False
            if len(prefix) != 2 or not prefix.isalpha():
                messagebox.showerror(
                    "Invalid command",
                    "Prefixes cannot be empty and must be two alphabetic characters.",
                )
                return False
            if prefix in used_prefixes:
                messagebox.showerror("Invalid command", "Prefixes must be unique.")
                return False
            used_prefixes.append(prefix)
        return True
