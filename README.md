**Nota:** [Leia a versão em português deste arquivo](https://github.com/lkotlarenko/gramma/blob/main/README_PT-BR.md)

# Gramma: Revolutionize Your Writing Anywhere with AI

Gramma is an innovative Python application that transforms your clipboard into a smart text assistant. With its advanced clipboard monitoring capabilities, Gramma identifies specific command prefixes within your copied text. Upon recognition, it seamlessly interacts with the GROQ API, utilizing tailored prompts to enhance and refine your text. Whether you’re looking to correct grammatical errors, condense lengthy articles, or creatively process content in ways only limited by your imagination, Gramma is your go-to solution. It’s easy to add new commands and ways of processing!

Designed with efficiency in mind, Gramma ensures a lightweight footprint, guaranteeing a negligible impact on your system’s performance. Elevate your writing and content creation with Gramma – where convenience meets intelligence.

## Default Commands

Gramma comes with a set of default commands to enhance your text processing experience. Below is a list of the default commands you can use:

- `!gf` - **Grammar Fix**: Enhances grammar in your text.
  ```
  !gf I can’t hardly believe I’m seing this!
  ```
  Result:
  ```
  I can hardly believe I’m seeing this!
  ```

- `!sm` - **Summarize**: Generates a succinct summary of the text.
  ```
  !sm The quick brown fox jumps over the lazy dog...
  ```
  Result:
  ```
  Summarized text.
  ```

- `!tl` - **Translate**: Translates the provided text.
  ```
  !tl Oi, como vai o seu dia?
  ```
  Result:
  ```
  Hi, how is your day?
  ```

- `!df` - **Define**: Provides a definition of a given word or expression.
  ```
  !df serendipity
  ```
  Result:
  ```
  The occurrence of events by chance in a happy or beneficial way.
  ```

## Adding or Editing Commands

Adding new commands or editing existing ones in Gramma is straightforward. Follow these steps:

1. **Add or Edit Commands**:
    - **Locate the `commands.py` file.**
    - To add a new command, add a new entry to the `commands` dictionary with the appropriate key and prompt. The key should follow the format `PROMPT_<COMMAND>`.
    - To edit an existing command, locate the desired command in the `commands` dictionary and modify its prompt.

    Example:
    ```python
    commands = {
        "PROMPT_GF": "You are a multi-language grammar enhancement tool...",
        "PROMPT_SM": "You are a multi-language AI designed to summarize text...",
        "PROMPT_TL": "You are a multi-language AI designed to translate text...",
        "PROMPT_DF": "You are a multi-language AI designed to define words...",
        "PROMPT_MW": "You are a tool that catfy text, output the received text in a cat-like form."
    }
    ```

2. **Save the File**: After adding or editing the command, save the `commands.py` file.
3. **Restart Gramma**: For the changes to take effect, restart Gramma by closing the application and running it again.
4. **Invoke your new command**: Now you can use the new command prefix. For example, copying:
    ```
    !mw I'm really cool, I like books, movies, and games.
    ```
    Will result in something similar to:
    ```
    Meowww, I'm reawy cowl, I wuv bookz, moviez and gamz! *rubs against leg*
    ```

By following these steps, you can easily customize Gramma to suit your specific needs and add new functionality as required.

## How It Works

1. **Clipboard Monitoring**: Continuously monitors the clipboard for changes.
2. **Command Detection**: Checks if the clipboard text starts with any predefined command prefixes.
3. **API Interaction**: Sends the text (excluding the command prefix) to the GROQ API with a corresponding custom prompt.
4. **Text Processing**: The AI processes the text and returns the modified version.
5. **Clipboard Update**: The processed text is copied back to the clipboard.
6. **Notification**: Displays a notification about the successful processing of the text.

## Features

- **Dynamic Command Loading**: Easily add new commands via `commands.py`.
- **Fully Free and Open source**: View and modify anything without any limits.
- **Privacy Focus**: No clipboard data is processed outside of command prefixes.
- **Asynchronous API Calls**: Efficiently handle API requests without blocking the main thread.
- **Minimalist Design**: No interface, only a system tray icon with an exit option.
- **Error Handling and Notifications**: Informative notifications for errors and rate limiting.

## Requirements

- Python 3.7+
- Groq API key (get one for free [here](https://console.groq.com/keys))

## Installation

1. **Install Python**

Ensure you have the latest version of Python installed. Download it from the [official Python website](https://www.python.org/downloads/).

1.5. **(Optional) Install GIT**

Ensure you have the latest version of GIT installed. Download it from the [official GIT website](https://git-scm.com/downloads).

#### Open a terminal (type `cmd` in the Explorer path of any folder you want to install Gramma on Windows) to run the following instructions:

1. **Clone the Repository** (if you haven't installed git, you can download it manually by clicking on `<> Code` and `Download ZIP` (on top of this page), and extract everything into a folder)


```sh
git clone https://github.com/lkotlarenko/gramma.git
cd gramma
```

3. **Create and Activate a Virtual Environment**

```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4. **Install the Required Packages**

```sh
pip install -r requirements.txt
```

5. **Configure Environment Variables**

Rename `.env.example` to `.env`:

```sh
mv .env.example .env
```

Edit the `.env` file with your API_KEY from Groq, replacing `YOUR_GROQ_API_KEY` with your actual key from [GROQ console](https://console.groq.com/keys) (you can edit it using notepad).

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

## Project Structure

```plaintext
gramma/
│
├── src/
│   ├── images/        # Folder to store app images (only the icon at the moment)
│   └── config.py      # Variables like app_name and more
├── .env               # Environment variables (where you put your API key)
├── requirements.txt   # Project dependencies
├── gramma.py          # Main script
├── gramma_starter.bat # Bat file to start Gramma in the system tray (create a shortcut to it to launch it faster)
├── README.md          # Project documentation (what you are reading right now)
└── README_PT-BR.md    # Project documentation in Brazilian Portuguese
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Author

Created by [lkotlarenko](https://github.com/lkotlarenko).

## License

This project is licensed under the MIT License.

## Links

- [GROQ Website](https://groq.com/)
