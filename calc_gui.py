import tkinter as tk


def click(value):
    current = screen.get()
    if value == "=":
        try:
            result = str(eval(current))
            screen.set(result)
        except:
            screen.set("Error")
    elif value == "C":
        screen.set("")
    elif value == "DEL":
        screen.set(current[:-1])
    else:
        screen.set(current + value)


def key_press(event):
    key = event.keysym
    char = event.char

    if key == "Return":
        button_refs["="].invoke()
    elif key == "BackSpace":
        button_refs["DEL"].invoke()
    elif key == "Escape":
        button_refs["C"].invoke()
    elif key == "KP_Decimal":
        button_refs["."].invoke()
    elif char == '.' or char == ',':
        button_refs["."].invoke()
    elif char in button_refs:
        button_refs[char].invoke()


def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        bg_color = "#222222"
        fg_color = "#f0f0f0"
        btn_bg = "#333333"
        btn_fg = "#f0f0f0"
        entry_bg = "#222222"
        dark_mode_button.config(text="☀️")  # sun icon
    else:
        bg_color = "white"
        fg_color = "black"
        btn_bg = "SystemButtonFace"
        btn_fg = "SystemButtonText"
        entry_bg = "white"
        dark_mode_button.config(text="🌙")  # moon icon

    root.configure(bg=bg_color)
    display.config(bg=entry_bg, fg=fg_color)
    dark_mode_button.config(bg=btn_bg, fg=btn_fg,
                            activebackground=btn_bg, activeforeground=btn_fg)
    button_frame.config(bg=bg_color)
    for btn in button_refs.values():
        btn.config(bg=btn_bg if dark_mode else "SystemButtonFace",
                   fg=btn_fg if dark_mode else "SystemButtonText",
                   activebackground=btn_bg if dark_mode else "SystemButtonFace",
                   activeforeground=btn_fg if dark_mode else "SystemButtonText")
    for child in button_frame.winfo_children():
        child.config(bg=bg_color)
    spacer.config(bg=bg_color)
    top_frame.config(bg=bg_color)


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x520")

dark_mode = False

# Top frame to hold toggle button right-aligned
top_frame = tk.Frame(root, bg=root["bg"])
top_frame.pack(fill="x", pady=(5, 0), padx=10)

spacer = tk.Label(top_frame, text="", bg=root["bg"])
spacer.pack(side="left", expand=True)

dark_mode_button = tk.Button(top_frame, text="🌙", font=("Arial", 14), width=3, relief="raised", bd=2,
                             command=toggle_dark_mode)
dark_mode_button.pack(side="right")

screen = tk.StringVar()
display = tk.Label(root, textvariable=screen, font="Arial 24", anchor='e',
                   bg="white", relief="sunken", height=2)
display.pack(fill="both", padx=10, pady=10)

button_frame = tk.Frame(root)
button_frame.pack(expand=True, fill="both")

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "DEL", "=", "+"],
    ["(", ")", ".", "C"]
]

button_refs = {}

for row in buttons:
    row_frame = tk.Frame(button_frame)
    row_frame.pack(expand=True, fill="both")
    for item in row:
        btn = tk.Button(row_frame, text=item, font="Arial 18", height=2, width=5)
        btn.pack(side="left", expand=True, fill="both")
        btn.config(command=lambda val=item: click(val))
        button_refs[item] = btn

root.bind("<Key>", key_press)

root.mainloop()
