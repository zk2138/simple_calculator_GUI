# Simple Calculator with GUI

A simple calculator application built with Python and Tkinter.  
Supports basic arithmetic operations, parentheses, keyboard input, and includes a dark mode toggle with icon.

---

## Features

- Addition, subtraction, multiplication, and division  
- Parentheses support for complex expressions  
- Keyboard input support (numbers, operators, parentheses)  
- Decimal point support for both `.` and `,` keys (useful for different keyboard layouts)  
- Backspace (DEL), Clear (C), and Enter (=) keys support via keyboard  
- Dark mode toggle button with moon/sun icons, positioned at the top-right corner  
- Responsive GUI with buttons and display area  

---

## Requirements

- Python 3.x (tested with Python 3.12)  
- Tkinter (usually comes bundled with Python)  

---

## How to Run

1. Save the Python code in a file named, for example, `calculator.py`.

2. Run the script in your terminal or command prompt:

   ```bash
   python calculator.py
   ```

3. The calculator window will appear. You can use both mouse clicks and keyboard input.

---

## Keyboard Controls

| Key          | Function                  |
|--------------|---------------------------|
| `0`-`9`      | Input digits              |
| `+`, `-`, `*`, `/` | Arithmetic operators |
| `(`, `)`     | Parentheses               |
| `.` or `,`   | Decimal point             |
| `Enter`      | Calculate result (`=`)    |
| `Backspace`  | Delete last character (`DEL`) |
| `Escape`     | Clear input (`C`)         |

---

## Dark Mode

- Toggle the dark mode using the button with the moon (🌙) / sun (☀️) icon at the top-right corner.  
- The colors of the interface and buttons update accordingly.

---

## Code Overview

- `click(value)`: Handles button presses and updates the calculator display or evaluates expressions.  
- `key_press(event)`: Maps keyboard presses to button actions.  
- `toggle_dark_mode()`: Switches between light and dark themes and updates the UI colors.  
- The GUI is constructed with Tkinter frames, buttons, and labels, arranged to fill the window responsively.

---

## License

This project is provided for educational and personal use.

---

Enjoy your calculations! 🎉
