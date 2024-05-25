🌐 Leia a versão em português deste arquivo [aqui](https://github.com/lkotlarenko/gramma/blob/main/README_PT-BR.md).

# Gramma: Transform your CTRL-C / CTRL-V into a Smart Text Assistant

Gramma is an innovative Python app that transforms your clipboard into a smart text assistant. With its advanced clipboard monitoring capabilities, Gramma identifies specific command prefixes within your copied text. Upon recognition, it seamlessly interacts with the GROQ AI API, utilizing tailored prompts to enhance and refine your text. Whether you're looking to correct grammatical errors, condense lengthy articles, or creatively process content in various ways, Gramma is your go-to solution.

## Features

- **Dynamic Command Loading**: Easily add new commands using a simple GUI interface.
- **Fully Free and Open Source**: View and modify anything without any limits.
- **Privacy Focus**: Clipboard data is processed ONLY IF a command prefix is detected.
- **Minimalist Design**: Lightweight and focused on ease to use.
- **Notifications**: Informative notifications.

## Requirements

- Python 3.7+
- Groq API key (get one for free [here](https://console.groq.com/keys))

## Installation

1. **Install Python**

   Ensure you have the latest version of Python installed. Download it from the [official Python website](https://www.python.org/downloads/).

2. **Download the Source Code**
   
   Visit the [latest release](https://github.com/lkotlarenko/gramma/releases/latest) and download the "Source code (zip)" file.
   
3. **Extract the Zip File**
   
   Extract the contents of the downloaded zip file to a directory of your choice.
   
4. **Install Dependencies**
   
   For Windows:
   - Open the extracted folder and double-click on `install_windows.bat`.
   - A terminal window will open and automatically install the required dependencies and create a desktop shortcut for Gramma.
   
   For Linux/macOS:
   - Open a terminal and navigate to the extracted folder.
   - Run the following command: `bash install_linux.sh`
   - This will install the required dependencies and create a desktop shortcut for Gramma.

## Setup

After installation, run the newly created Gramma shortcut in your desktop, you will find the Gramma icon in your system tray (notification area).

1. **Right-click** on the Gramma icon in the system tray.
2. Select **"Setup"**.
3. Enter your **GROQ API Key** (get one for free [here](https://console.groq.com/keys)).
4. (Optional) Change the **AI Model** if desired (see the available ones [here](https://console.groq.com/docs/models)).
5. Click **"Save"**.
6. Confirm

Gramma is now ready to use!

## Usage

1. **Copy text** to your clipboard with one of the command prefixes (e.g., `!gf Your text here` for grammar correction).
2. **Wait for the notification** indicating that the text has been processed.
3. The processed text will be automatically copied back to your clipboard.

## Default Commands

Gramma comes with a set of default commands to enhance your text processing experience:

- `!gf` - **Grammar Fix**: Enhances grammar in your text.
- `!sm` - **Summarize**: Generates a succinct summary of the text.
- `!tl` - **Translate**: Translates the provided text.
- `!df` - **Define**: Provides a definition of a given word or expression.

## Adding or Editing Commands

Adding new commands or editing existing ones in Gramma is straightforward:

1. **Right-click** on the Gramma icon in the system tray.
2. Select **"Edit Commands"**.
3. In the "Edit Commands" window, you can:
   - **Add a new command**: Click the "Add Command" button and enter the command prefix and prompt (the prefix is only two letters that are not in use by other prefixes).
   - **Edit an existing command**: Modify commands prefix or prompt as desired.
   - **Delete a command**: Delete any command from the list by clicking on the red "X" button.
4. Click **"Save"** to apply the changes.
5. Confirm

The new or edited commands will be available for use immediately.

## How It Works

1. **Clipboard Monitoring**: Gramma continuously monitors the clipboard for changes.
2. **Command Detection**: It checks if the clipboard text starts with any predefined command prefixes.
3. **API Interaction**: Gramma sends the text (excluding the command prefix) to the GROQ AI API with a corresponding custom prompt.
4. **Text Processing**: The AI processes the text and returns the modified version.
5. **Clipboard Update**: The processed text is copied back to the clipboard.
6. **Notification**: A notification is displayed about the successful processing of the text.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Author

Created by [lkotlarenko](https://github.com/lkotlarenko).

### Support Me

If you liked my work and want to support me, you can sponsor me here on GitHub. Your support will enable me to focus more on open-source projects. Those contributions will help me continue to learn, grow, and contribute to the open-source ecosystem 💚.

[![GitHub Sponsors](https://img.shields.io/github/sponsors/lkotlarenko?style=social)](https://github.com/sponsors/lkotlarenko)

## License

This project is licensed under the [MIT License](LICENSE).

## Links

- [Groq Website](https://groq.com/)
- [Groq Console](https://console.groq.com/)

## Project Structure

```plaintext
gramma/
│
├── src/
│   ├──core/
│   │  ├── clipboard_listener.py
│   │  ├── command_processor.py
│   │  ├── instance_manager.py
│   │  └── tray_icon.py
│   │
│   ├── data/
│   │   ├── __init__.py
│   │   └── data_manager.py
│   │
│   ├── gui/
│   │   ├── base_page.py
│   │   ├── edit_commands_page.py
│   │   └── setup_page.py
│   │
│   ├── images/
│   │   ├── app_icon.ico
│   │   └── tray_icon.png
│   │
│   ├── managers/
│   │   └── instance_manager.py
│   │
│   ├── utils.py
│   └── config.py
│
├── tests/
│   ├──core/
│   │  └── __init__.py
│   │
│   ├── data/
│   │   ├── __init__.py
│   │   └── test_data_manager.py
│   │
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── edit_commands_page.py
│   │   └── setup_page.py
│   ├── __init__.py
│   └── conftest.py
│
├── commands.json
├── gramma.py
├── install_linux.sh
├── install_windows.bat
├── gramma_starter_linux.sh
├── gramma_starter.bat
├── gramma_to_tray_win.vbs
├── LICENSE
├── poetry.lock
├── pyproject.toml
├── README.md
├── README_PT-BR.md
└── settings.json
```