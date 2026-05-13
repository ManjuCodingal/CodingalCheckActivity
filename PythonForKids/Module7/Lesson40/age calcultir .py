from tkinter import *
from datetime import date

def calculate_age():
    try:
        name = entry_name.get()
        d = int(entry_day.get())
        m = int(entry_month.get())
        y = int(entry_year.get())

        today = date.today()
        birth_date = date(y, m, d)

        age = today.year - birth_date.year

        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result_label.config(text=f"Hello {name}, you are {age} years old.")

    except ValueError:
        result_label.config(text="Please enter valid details!")

# Main window
root = Tk()
root.title("Age Calculator App")
root.geometry("400x400")

# Title label
Label(root, text="Age Calculator", font=("Arial", 16, "bold")).pack(pady=10)

# Frame for inputs (for side-by-side layout)
frame = Frame(root)
frame.pack(pady=10)

# Name
Label(frame, text="Name").grid(row=0, column=0, padx=10, pady=5)
entry_name = Entry(frame)
entry_name.grid(row=0, column=1, padx=10, pady=5)

# Day
Label(frame, text="Day").grid(row=1, column=0, padx=10, pady=5)
entry_day = Entry(frame)
entry_day.grid(row=1, column=1, padx=10, pady=5)

# Month
Label(frame, text="Month").grid(row=2, column=0, padx=10, pady=5)
entry_month = Entry(frame)
entry_month.grid(row=2, column=1, padx=10, pady=5)

# Year
Label(frame, text="Year").grid(row=3, column=0, padx=10, pady=5)
entry_year = Entry(frame)
entry_year.grid(row=3, column=1, padx=10, pady=5)

# Button
Button(root, text="Calculate Age", command=calculate_age, bg="lightblue").pack(pady=15)

# Result
result_label = Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()