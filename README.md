**Note:** [Leia a versão em português deste arquivo](https://github.com/lkotlarenko/gramma/blob/main/README_PT-BR.md)

# Gramma: Revolutionize Your Writing Anywhere with AI.

Gramma is an innovative Python application that transforms your clipboard into a smart text assistant. With its advanced clipboard monitoring capabilities, Gramma identifies specific command prefixes within your copied text. Upon recognition, it seamlessly interacts with the GROQ API, utilizing tailored prompts to enhance and refine your text. Whether you’re looking to correct grammatical errors, condense lengthy articles, or creatively process content in ways only limited by your imagination, Gramma is your go-to solution. It’s really easy to add new commands and ways of processing!

Designed with efficiency in mind, Gramma ensures a lightweight footprint, guaranteeing a negligible impact on your system’s performance. Elevate your writing and content creation with Gramma – where convenience meets intelligence.

## How It Works

1. **Clipboard Monitoring**: The script continuously monitors the clipboard for changes.
2. **Command Detection**: When a change is detected, it checks if the clipboard text starts with any of the predefined command prefixes.
3. **API Interaction**: If a command is detected, the script sends the text (excluding the command prefix) to the GROQ API with a corresponding custom prompt.
4. **Text Processing**: The AI processes the text and returns the modified version.
5. **Clipboard Update**: The processed text is copied back to the clipboard.
6. **Notification**: The user receives a notification about the successful processing of the text.

## Features

- **Dynamic Command Loading**: Easily add new commands via environment variables.
- **Asynchronous API Calls**: Efficiently handle API requests without blocking the main thread.
- **Minimalism**: The app has no interface, only a system tray icon with an option to exit, since the app is designed to be used at any time, with no interference in your focus.
- **Error Handling and Notifications**: Informative notifications for errors and rate limiting.

## Requirements

- Python 3.7+
- `pyperclip`
- `python-dotenv`
- `groq`
- `pystray`
- `pillow`
- `plyer`

## Installation

### 1. Install Python

Ensure you have the latest version of Python installed. Download it from the [official Python website](https://www.python.org/downloads/).

### 1.5. (OPTIONAL) Install GIT

Ensure you have the latest version of GIT installed. Download it from the [official GIT website](https://git-scm.com/downloads).

#### Open a terminal (type `cmd` in the Explorer path of any folder you want to install Gramma on windows) to run the following instructions:

### 2. Clone the Repository (you can do it manually too by clicking on `<> Code` and `Download ZIP` in case you don't want to install git, make sure you extract the files to a folder somewhere)

```sh
git clone https://github.com/yourusername/gramma.git
cd gramma
```

### 3. Create and Activate a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Install the Required Packages

```sh
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Rename `.env.example` to `.env`:

```sh
mv .env.example .env
```

Edit the `.env` file with your API_KEY from Groq, replacing `YOUR_GROQ_API_KEY` with your actual key from [GROQ console](https://console.groq.com/keys):

### It should look something like this after editing:

```env
GROQ_API_KEY=gsk_y**********************************************
```

## Usage

### Start the Clipboard Listener

You can create a shortcut for the file `gramma_starter.bat` and move it to any place to run Gramma.

### Tray Icon

The script will minimize to the system tray. Right-click the tray icon for exiting.

### Using Commands

Copy text to your clipboard with one of the command prefixes (e.g., `!gf Your text here` for grammar correction).

## Adding New Commands

To add new commands, simply add new environment variables in your `.env` file with the `PROMPT_` prefix. For example:

```env
PROMPT_MW=You are a tool that catfy text, output the received text in a cat like form.
```

Save the file and run Gramma again, you should be able to invoke it with your new prefix, in this case `!mw`. Here is it in action:

```plaintext
!mw I'm really cool, I like books, movies, and games.
```

Should generate something like:

```plaintext
Meowww, I'm reawy cowl, I wuv bookz, moviez and gamz! *rubs against leg*
```

## Project Structure

```plaintext
gramma/
│
├── .env              # Environment variables
├── requirements.txt  # Project dependencies
├── script.py         # Main script
├── gramma_starter.bat # Bat file to start Gramma in the system tray
└── README.md         # Project documentation (what you are reading right now)
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Author

Created by [lkotlarenko](https://github.com/lkotlarenko).

## License

This project is licensed under the MIT License.

## Links

- [GROQ Website](https://groq.com/)
