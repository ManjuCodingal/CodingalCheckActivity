from tkinter import *

window = Tk()

window.title("Length Converter App")
window.geometry("400x400")
window.config(bg="#f0f8ff")

title = Label(
    window,
    text="Password Strength Checker",
    font=("Arial", 18, "bold"),
    bg="#f0f8ff",
    fg="#333333"
)
title.pack(pady=20)

label = Label(
    window,
    text="Enter Password:",
    font=("Arial", 12),
    bg="#f0f8ff"
)
label.pack()

entry = Entry(
    window,
    font=("Arial", 14),
    width=20,
    show="*",
    bd=3
)
entry.pack(pady=10)

result = Label(
    window,
    text="",
    font=("Arial", 16, "bold"),
    bg="#f0f8ff"
)
result.pack(pady=20)

def check_strength():
    password = entry.get()
    length = len(password)

    if length <= 5:
        result.config(text="Weak", fg="red")

    elif length <= 8:
        result.config(text="Medium", fg="yellow")

    elif length <= 12:
        result.config(text="Strong", fg="light green")

    else:
        result.config(text="Very Strong", fg="dark green")

button = Button(
    window,
    text="Check Strength",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5,
    command=check_strength
)
button.pack(pady=10)

window.mainloop()