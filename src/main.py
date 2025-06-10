import tkinter as tk
from langdetect import detect, DetectorFactory
from langdetect import LangDetectException

# Dictionary to map ISO language codes to friendlier readable names for the user
LANGUAGE_NAMES = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'pt': 'Portuguese',
    'ru': 'Russian',
    'ar': 'Arabic',
    'zh-cn': 'Chinese (Simplified)',
    'ja': 'Japanese',
    'ko': 'Korean',
    'nl': 'Dutch',
    'pl': 'Polish',
    'sv': 'Swedish',
    'tr': 'Turkish',
    'fa': 'Persian',
    'hi': 'Hindi'
    # We can add more as needed
}

# Button logic
def detect_language():
    # Get text from the Text Widget and clean it
    text = text_input.get("1.0", tk.END).strip() # from line 1, char 0 to end

    # Input validation: if it's too short, show a warning
    if len(text) < 3:
        result_label.config(text="❌ Please enter more text for reliable detection.", fg="red")
        return
    
    try:
        # Detect the language
        lang_code = detect(text) # returns the ISO 639-1 language code (e.g., 'en' for English).
        lang_name = LANGUAGE_NAMES.get(lang_code, "Unknown") # Map code to name
        result_label.config(text=f"✅ Detected language: {lang_name} ({lang_code})", fg="green")
    except LangDetectException:
        # Handle detection errors
        result_label.config(text="❌ Could not detect language. Try different text.", fg="red")

def clear_text():
    text_input.delete("1.0", tk.END) # Clear all text in the input box
    result_label.config(text="")  # Clear the result label
    text_input.focus()  # Set focus back to the text input box after clearing

def clear_result_on_typing(event):
    result_label.config(text="")  # Clear the result label when the user starts typing

# Setting a seed: Ensure consistent detection results and avoid randomness
DetectorFactory.seed = 0

# Main window
root = tk.Tk()
root.title("Language Detector")
root.geometry("500x300")

# Instructions
instructions = tk.Label(root, text="Past or type text below and press Detect", font=("Arial", 12))
instructions.pack(pady=10)

# Text box (multi-line)
text_input = tk.Text(root, height=6, width=60, font=("Arial", 11))
text_input.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("arial", 12))
result_label.pack(pady=10)

# Detect button
detect_button = tk.Button(root, text="Detect language", command=detect_language)
detect_button.pack(pady=10)

# Clear button
clear_button = tk.Button(root, text="Clear", command=clear_text)
clear_button.pack(pady=2)

# Enter (return) key binding to detect language
root.bind('<Return>', lambda event: detect_language())

# Clear the result when typing
text_input.bind('<Key>', clear_result_on_typing)

text_input.focus()  # Automatically focus the text input box when the app starts

# Start the app
root.mainloop()