import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Create a translator object
translator = Translator()

# Function to translate text to a specific language
def translate_text():
    text_to_translate = source_text.get()
    target_language = target_language_combo.get()
    
    try:
        translated = translator.translate(text_to_translate, dest=target_language)
        translated_text.delete(1.0, tk.END)  # Clear any previous text
        translated_text.insert(tk.END, translated.text)
    except Exception as e:
        translated_text.delete(1.0, tk.END)
        translated_text.insert(tk.END, "Translation Error")

# Function to list available languages
def list_languages():
    available_languages.delete(1.0, tk.END)  # Clear any previous list
    available_languages.insert(tk.END, "Available Languages:\n")
    for code, lang in LANGUAGES.items():
        available_languages.insert(tk.END, f"{code}: {lang}\n")

# Create the main application window
app = tk.Tk()
app.title("Language Translator")

# Create and configure GUI elements
source_label = ttk.Label(app, text="Source Text:")
source_text = ttk.Entry(app, width=40)

target_lang_label = ttk.Label(app, text="Target Language:")
target_language_combo = ttk.Combobox(app, values=list(LANGUAGES.keys()))

translate_button = ttk.Button(app, text="Translate", command=translate_text)

translated_text_label = ttk.Label(app, text="Translated Text:")
translated_text = tk.Text(app, height=6, width=40)

available_languages = tk.Text(app, height=10, width=40)

list_languages()  # Populate the available languages list initially

# Arrange GUI elements using grid layout
source_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
source_text.grid(row=0, column=1, padx=10, pady=5)

target_lang_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
target_language_combo.grid(row=1, column=1, padx=10, pady=5)

translate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

translated_text_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
translated_text.grid(row=3, column=1, padx=10, pady=5)

available_languages_label = ttk.Label(app, text="Available Languages:")
available_languages_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
available_languages.grid(row=4, column=1, padx=10, pady=5)

# Start the GUI application
app.mainloop()
