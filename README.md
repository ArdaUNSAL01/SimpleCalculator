# 🧮 Simple Calculator (Python & Tkinter)

> **Note:** This project was developed for educational purposes to practice and learn the Python Tkinter library, specifically focusing on the `grid` layout manager and event handling.

A functional and colorful calculator application built with Python. This tool performs basic arithmetic operations and features a **dynamic theme changer** that allows users to customize the background color on the fly.

## 🚀 Features

* **Standard Arithmetic:** Supports addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
* **Grid Layout:** Uses Tkinter's `grid()` geometry manager for a precise, matrix-like button arrangement similar to physical calculators.
* **One-Touch Calculation:** Utilizes Python's powerful evaluation capabilities to process equations instantly.
* **Error Handling:** Displays a "Hata" (Error) message if the user tries invalid operations (like dividing by zero).
* **Theme Customization:** Includes a "Renk Değiştir" (Change Color) button that opens a color palette, allowing users to personalize the application background.

## 🧠 How It Works

This project demonstrates three key programming concepts:

1.  **The `eval()` Function:**
    * Instead of writing separate functions for every math operation, the program takes the entire equation string from the screen (e.g., "5+3*2") and uses Python's built-in `eval()` function to calculate the result automatically.
2.  **Grid Geometry Manager:**
    * Unlike the `pack()` method which stacks widgets, this project uses `.grid(row=x, column=y)`. This aligns buttons perfectly in rows and columns.
3.  **Lambda Functions:**
    * The buttons use `lambda: yaz("1")` commands. This allows passing specific arguments (like the number 1, 2, or +) to the main function when a button is clicked.
4.  **Color Chooser:**
    * The `renk_degistir` function calls `colorchooser.askcolor()`, which opens the operating system's default color picker and applies the selected color to the window background.

## 🛠️ Requirements

* Python 3.x
* Tkinter (Included with standard Python installations)

## 💻 Usage

1.  Clone or download the repository.
2.  Run the Python script:
    ```bash
    python calculator.py
    ```
3.  Click the number buttons and operation signs to form an equation.
4.  Press **"="** to see the result.
5.  Press **"C"** to clear the screen.
6.  Click **"Renk Değiştir"** to pick a new background color for your calculator.

---
**Author:** [Arda ÜNSAL]
