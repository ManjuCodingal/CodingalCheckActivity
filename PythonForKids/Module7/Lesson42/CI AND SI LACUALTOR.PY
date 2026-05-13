from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Interest Calculator App")
window.geometry("400x400")
window.config(bg="#1e1e2f")

heading = Label(
    window,
    text="Interest Calculator",
    font=("Helvetica", 20, "bold"),
    bg="#1e1e2f",
    fg="#00ffd5"
)
heading.pack(pady=15)

frame = Frame(window, bg="#2b2b45", bd=3, relief=RIDGE)
frame.pack(pady=20, padx=20)

Label(
    frame,
    text="Principal Amount",
    font=("Arial", 12, "bold"),
    bg="#2b2b45",
    fg="white"
).grid(row=0, column=0, padx=10, pady=10, sticky="w")

principal_entry = Entry(
    frame,
    font=("Arial", 12),
    width=18,
    bd=3,
    relief=GROOVE
)
principal_entry.grid(row=0, column=1, padx=10, pady=10)

Label(
    frame,
    text="Time Years",
    font=("Arial", 12, "bold"),
    bg="#2b2b45",
    fg="white"
).grid(row=1, column=0, padx=10, pady=10, sticky="w")

time_entry = Entry(
    frame,
    font=("Arial", 12),
    width=18,
    bd=3,
    relief=GROOVE
)
time_entry.grid(row=1, column=1, padx=10, pady=10)

Label(
    frame,
    text="Rate of Interest",
    font=("Arial", 12, "bold"),
    bg="#2b2b45",
    fg="white"
).grid(row=2, column=0, padx=10, pady=10, sticky="w")

rate_entry = Entry(
    frame,
    font=("Arial", 12),
    width=18,
    bd=3,
    relief=GROOVE
)
rate_entry.grid(row=2, column=1, padx=10, pady=10)


def calculate_interest():
    try:
        p = float(principal_entry.get())
        t = float(time_entry.get())
        r = float(rate_entry.get())

        si = p * t * r / 100

        amount = p * (1 + r / 100) ** t
        ci = amount - p

        result_label.config(
            text=f"Simple Interest = ₹{si:.2f}\nCompound Interest = ₹{ci:.2f}",
            fg="#00ff99"
        )

    except:
        messagebox.showerror("Invalid Input", "Please enter valid numbers!")


calc_button = Button(
    window,
    text="Calculate",
    font=("Arial", 13, "bold"),
    bg="#00ffd5",
    fg="black",
    padx=15,
    pady=5,
    relief=RAISED,
    command=calculate_interest
)
calc_button.pack(pady=15)

result_label = Label(
    window,
    text="",
    font=("Arial", 14, "bold"),
    bg="#1e1e2f",
    fg="white"
)
result_label.pack(pady=20)

window.mainloop()