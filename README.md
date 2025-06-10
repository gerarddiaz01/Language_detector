# Language Detector 🈯

This is a beginner-friendly Python GUI application that detects the language of a given text using the langdetect library. Users type or paste any text, and the app will display the name and ISO code of the detected language. It’s fast, simple, and responsive — and designed with learners in mind.

What makes this project stand out is not just that it works, but how it was built — with a focus on good UX, clean architecture, and personal growth. The goal here wasn’t perfection, but progress.

---

## Teaching Perspective 📚

I was learning myself while making the script, well into my third month of Python learning. This project is intentionally written with learners in mind. If you're exploring tkinter, text analysis, or GUI-based validation — you’ll find this helpful as a reference or a foundation for your own ideas.
You can use it to:
   - Learn GUI layout basics
   - Understand library integration with a frontend
   - See how small design details improve UX

---

## How to Run the Application 🚀

1. **Install Dependencies**:
   - Install the required libraries by running the following command in your terminal:
     ```
     pip install -r requirements.txt
     ```

2. **Run the Script**:
   - Open a terminal or command prompt, navigate to the folder containing `main.py`, and run the following command:
     ```
     python src/main.py
     ```

3. **Use the Application**:
   - Type or paste text into the input box and click the "Detect language" button or press Enter to detect the language.
   - Use the "Clear" button to reset the input field and result label.

---

## Features ✨

1. **Language Detection**:
   - Detects the language of the input text and displays both the language name and its ISO 639-1 code.

2. **Input validation**:
   - In order to prevent short/invalid input.

3. **Clear Button**:
   - Resets the input and result fields for a fresh start.

4. **Keyboard Shortcut**:
   - Allows pressing Enter to trigger detection for better usability.

5. **Auto-Focus**:
   - Automatically focuses the text input box when the app starts.

6. **Dynamic Updates**:
   - Clears the result label when the user starts typing.

---

## Tools and Strategies Used 🛠️

1. **`tkinter`**:
   - Used to create the graphical user interface, including labels, buttons, and input fields.
   - Demonstrates the use of layout managers like `pack()` and event bindings like `bind()`.

2. **`langdetect`**:
   - Provides language recognition and returns both full name and code.
   - Handled gracefully with try/except for robustness

3. **Input Validation**:
   - Ensures the input is not empty and contains enough text for reliable detection.
   - Provides meaningful error messages for invalid input.

4. **Event Binding**:
   - Binds the Enter key to the `detect_language()` function, allowing users to trigger detection without clicking the button.
   - Clears the result field on keypress for responsiveness.

---

## Challenges Encountered and Solutions 🧩

1. **Detecting Short/Invalid Inputs**:
   - Challenge: Users could enter nonsense or 1-letter inputs.
   - Solution: Added a check for minimum input length and returned helpful messages.

2. **langdetect Exceptions**:
   - Challenge: Some inputs raised detection errors.
   - Solution: Wrapped detection in try/except and displayed user-friendly messages instead of crashes.

3. **Usability Friction**:
   - Challenge: Needing to click input manually or see old results still visible.
   - Solution: Auto-focused the text field and cleared results dynamically on new input.

---

## What I Learned 👨‍🎓

This project provided an opportunity to practice and improve several important skills:
- Built a complete GUI workflow using tkinter
- Practiced exception handling and validation techniques
- Improved UX with features like keyboard binding and auto-clear
- Explored how to combine a library (langdetect) with an interface
- Learned to structure and document code for future use and teaching

This was a fast, iterative project — but one where I made sure each part taught me something new.

---

## Conclusion 📝

This may be a small app, but it helped me internalize some key lessons in Python development. It’s not about flashy tools — it’s about making small things work well, learning from them, and communicating that clearly.

That’s the kind of developer I strive to be — and this project reflects that mindset.
