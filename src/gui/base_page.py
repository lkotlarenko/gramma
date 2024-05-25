import customtkinter as ctk
import os
from tkinter import messagebox
from PIL import Image, ImageTk
from src.data import SharedData


class BasePage(ctk.CTk):
    def __init__(self, shared_data: SharedData):
        super().__init__()
        self.shared_data = shared_data
        self.geometry("500x280")

        icon_path = os.path.join(os.getcwd(), "src/images", "icon.png")
        if os.path.exists(icon_path):
            try:
                self.icon = Image.open(icon_path)
                self.icon_img = ImageTk.PhotoImage(self.icon)
                self.iconphoto(True, self.icon_img)
            except Exception as e:
                print(f"Failed to load icon: {e}")
        else:
            print("Icon file not found.")

        self.create_ui()

    def create_ui(self):
        raise NotImplementedError("Subclasses must implement create_ui method.")

    def validate_input(self):
        raise NotImplementedError("Subclasses must implement validate_input method.")

    def show_confirmation_dialog(self, title, message):
        return messagebox.askyesno(title, message)
