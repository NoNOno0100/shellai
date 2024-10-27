import os
import openai
import json
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=1)

HISTORY_FILE = "history.jsonl"
CACHE_FILE = "conversation_cache.json"
openai.api_key = os.getenv("OPENAI_API_KEY")

def save_to_history_async(conversation):
    executor.submit(save_to_history, conversation)

def save_to_history(conversation):
    """Saves the conversation to the history file with a title and date."""
    conversation_entry = {
        "title": conversation.get("title", "Untitled"),
        "date": conversation.get("date", datetime.now().isoformat()),
        "messages": conversation["messages"]
    }
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        json.dump(conversation_entry, f, ensure_ascii=False)
        f.write("\n")

def load_history():
    """Loads the conversation history from the JSONL file, skipping malformed lines."""
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    history.append(json.loads(line))
                except json.JSONDecodeError:
                    print("Skipping malformed line in history file.")
    return history

def advanced_search():
    term = input("Enter a search term: ").lower()
    history = load_history()
    results = []

    for conversation in history:
        for msg in conversation["messages"]:
            if "content" in msg and term in msg["content"].lower():
                highlighted_msg = msg["content"].replace(term, f"\033[1;31m{term}\033[0m")
                results.append({
                    "title": conversation["title"],
                    "date": conversation["date"],
                    "role": msg.get("role", "Unknown Role"),
                    "message": highlighted_msg
                })

    if results:
        for res in results:
            print(f"\033[1;35mTitle:\033[0m {res['title']} \033[1;35mDate:\033[0m {res['date']}")
            print(f"\033[1;34m{res['role']}:\033[0m {res['message']}\n")
    else:
        print(f"No results found for '{term}'.")

def view_and_edit_history():
    history = load_history()
    if not history:
        print("No history available.")
        return
    for i, conv in enumerate(history):
        print(f"{i + 1}. {conv['title']} (Date: {conv['date']})")

    choice = input("\nChoose a conversation number to view or edit title (or 'exit' to go back): ")
    if choice.isdigit():
        conv_index = int(choice) - 1
        if 0 <= conv_index < len(history):
            conv = history[conv_index]
            print(f"\n\033[1;35mViewing Conversation '{conv['title']}' from {conv['date']}:\033[0m\n")
            for msg in conv["messages"]:
                role = msg.get("role", "Unknown Role")
                content = msg.get("content", "")
                print(f"\033[1;34m{role}:\033[0m {content}")

            new_title = input("\nEnter a new title for this conversation (or press Enter to keep current title): ")
            if new_title:
                conv["title"] = new_title
                save_to_history_async(conv)

def chat_natural():
    """Engages in a natural conversation with the user, saving upon exit."""
    conversation = {"title": "", "date": datetime.now().isoformat(), "messages": []}

    print("You are now in natural conversation mode. Type 'exit' to leave.")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                break

            conversation["messages"].append({"role": "user", "content": user_input})

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": msg["role"], "content": msg["content"]} for msg in conversation["messages"]]
            )

            assistant_reply = response.choices[0].message['content']
            print(f"\033[1;34mGPT:\033[0m {assistant_reply}")

            conversation["messages"].append({"role": "assistant", "content": assistant_reply})

        except (KeyboardInterrupt, EOFError):
            print("\nSession ended unexpectedly. Saving conversation.")
            if not conversation["title"]:
                conversation["title"] = conversation["messages"][0]["content"][:50] + "..."
            save_to_history_async(conversation)
            break

    if not conversation["title"]:
        conversation["title"] = input("Enter a title for this conversation: ") or conversation["messages"][0]["content"][:50] + "..."
    save_to_history_async(conversation)

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Natural Conversation Mode")
        print("2. View and Edit History")
        print("3. Advanced Search in History")
        print("4. Compress History File")
        print("5. Clean Cache")
        print("6. Exit")

        choice = input("Choose an option (1 to 6): ")

        if choice == "1":
            chat_natural()
        elif choice == "2":
            view_and_edit_history()
        elif choice == "3":
            advanced_search()
        elif choice == "4":
            compress_history_file()
        elif choice == "5":
            clean_cache()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

def compress_history_file():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "rb") as f_in:
            with open(HISTORY_FILE + ".gz", "wb") as f_out:
                f_out.write(f_in.read())
        print("History file compressed.")

def clean_cache():
    if os.path.exists(CACHE_FILE):
        os.remove(CACHE_FILE)
        print("Cache cleaned.")
    else:
        print("No cache to clean.")

if __name__ == "__main__":
    main_menu()
