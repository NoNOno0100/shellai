# shella

```markdown
# OpenAI Chat History Manager

### Description
This is a command-line tool for interacting with OpenAI's ChatCompletion API, enabling users to engage in natural conversations, save chat history, search through past conversations, and manage their data efficiently. The tool provides features for advanced search, history editing, and compression, making it easy to revisit and manage previous chat interactions.

## Features
- **Natural Conversation Mode:** Engage in a conversation with OpenAI's `gpt-3.5-turbo` model.
- **History Management:** View, edit, and rename saved conversations.
- **Advanced Search:** Search through conversation history for specific terms with highlighted results.
- **History Compression:** Compress history files to save disk space.
- **Cache Cleaning:** Easily clean up cache files.

## Table of Contents
1. [Installation](#installation)
2. [Configuration](#configuration)
3. [Usage](#usage)
    - [Running the Program](#running-the-program)
    - [Natural Conversation Mode](#natural-conversation-mode)
    - [Managing History](#managing-history)
    - [Advanced Search](#advanced-search)
    - [Compress History File](#compress-history-file)
    - [Clean Cache](#clean-cache)
4. [Code Structure](#code-structure)
5. [Troubleshooting](#troubleshooting)
6. [Contributing](#contributing)
7. [License](#license)

## Installation

### Prerequisites
- Python 3.7 or higher
- `pip` installed

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/openai-chat-history-manager.git
cd openai-chat-history-manager
```

### Step 2: Install Required Packages
```bash
pip install openai python-dotenv colorama
```

## Configuration

### Step 1: Set Up OpenAI API Key
Create a `.env` file in the root directory of the project and add your OpenAI API key:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

Replace `your_openai_api_key_here` with the API key you obtained from [OpenAI](https://platform.openai.com/account/api-keys).

## Usage

### Running the Program
To start the program, run:
```bash
python script.py
```

You will see the following main menu:
```plaintext
Main Menu:
1. Natural Conversation Mode
2. View and Edit History
3. Advanced Search in History
4. Compress History File
5. Clean Cache
6. Exit
Choose an option (1 to 6):
```

### Natural Conversation Mode
1. Select option `1` to start a conversation.
2. Type your message and press Enter.
3. To exit, type `exit` and press Enter.
4. After exiting, you will be prompted to save the conversation with a title.

### Managing History
1. Select option `2` from the main menu.
2. You will see a list of saved conversations.
3. Choose a conversation by entering its number to view or edit the title.
4. Press Enter to keep the existing title or enter a new one.

### Advanced Search
1. Select option `3` from the main menu.
2. Enter a search term to look for within the history.
3. The results will show all occurrences of the term, highlighted for easy reading.

### Compress History File
1. Select option `4` from the main menu.
2. The program will compress the history file, saving it as `history.jsonl.gz`.

### Clean Cache
1. Select option `5` from the main menu.
2. The cache file will be deleted if it exists.

## Code Structure
```
openai-chat-history-manager/
│
├── script.py              # Main script file with all the program logic.
├── .env                   # Configuration file for environment variables.
├── requirements.txt       # List of required Python packages.
├── history.jsonl          # Stores all the saved conversations.
└── conversation_cache.json # Temporary cache file (optional).
```

### Explanation:
- **`script.py`:** Contains the main functions for interacting with OpenAI and managing the conversation history.
- **`.env`:** Environment variables for secure storage of the OpenAI API key.
- **`history.jsonl`:** JSON Lines file format for easy appending of conversation data.
- **`conversation_cache.json`:** Temporary data storage that can be cleaned up using the menu option.

## Troubleshooting
- **Error: `No module named 'openai'`:**
  - Make sure you have installed the required packages using `pip install -r requirements.txt`.
- **Error: `OpenAI API key not set`:**
  - Double-check that your `.env` file is properly configured and the API key is correct.

## Contributing
Feel free to contribute by submitting issues, pull requests, or suggestions. Make sure to follow the coding guidelines and test your changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### הוראות נוספות
1. **קובץ `requirements.txt`:**
   ניתן ליצור קובץ `requirements.txt` שיכיל את החבילות הבאות להתקנה מהירה:
   ```plaintext
   openai
   python-dotenv
   colorama
   ```
   ואז אפשר להתקין את החבילות בצורה מסודרת עם:
   ```bash
   pip install -r requirements.txt
   ```

2. **קובץ `.gitignore`:**
   כדאי להוסיף `.gitignore` כדי למנוע מקבצים כמו `.env` להיכנס ל-repo שלך:
   ```
   .env
   __pycache__/
   *.pyc
   conversation_cache.json
   history.jsonl
   history.jsonl.gz
   ```

