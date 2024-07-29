import tkinter as tk
from tkinter import messagebox
import requests

def setup_window():
    root = tk.Tk()
    root.title("Dictionary App")
    root.geometry("400x300")
    return root

def create_input_field(root):
    tk.Label(root, text="Enter a word:").pack(pady=10)
    word_entry = tk.Entry(root, width=30)
    word_entry.pack(pady=10)
    return word_entry

def create_buttons(root, fetch_definition):
    search_button = tk.Button(root, text="Search", command=fetch_definition)
    search_button.pack(pady=10)
    return search_button

def create_definition_label(root):
    definition_label = tk.Label(root, text="", wraplength=350, justify="left")
    definition_label.pack(pady=20)
    return definition_label

def fetch_definition(word_entry, definition_label):
    word = word_entry.get().strip()
    if word:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            try:
                definition = data[0]['meanings'][0]['definitions'][0]['definition']
                definition_label.config(text=definition)
            except (IndexError, KeyError):
                definition_label.config(text="Definition not found!")
        else:
            definition_label.config(text="Word not found!")
    else:
        messagebox.showwarning("Warning", "Please enter a word.")

def main():
    root = setup_window()

    word_entry = create_input_field(root)
    definition_label = create_definition_label(root)
    search_button = create_buttons(root, lambda: fetch_definition(word_entry, definition_label))

    root.mainloop()

if __name__ == "__main__":
    main()
