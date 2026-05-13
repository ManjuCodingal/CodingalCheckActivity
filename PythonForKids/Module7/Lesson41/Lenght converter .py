# import tkinter as tk

# def convert():
#     try:
#         inches = float(entry.get())
#         centimeters = inches * 2.54
#         result_label.config(text=f"{centimeters:.2f} cm")
#     except ValueError:
#         result_label.config(text="Enter a valid number")

# root = tk.Tk()
# root.title("Inches to Centimeters Converter")
# root.geometry("400x400")

# label = tk.Label(root, text="Enter length in inches:")
# label.pack(pady=10)

# entry = tk.Entry(root)
# entry.pack(pady=5)

# convert_button = tk.Button(root, text="Convert", command=convert)
# convert_button.pack(pady=10)

# result_label = tk.Label(root, text="")
# result_label.pack(pady=10)

# root.mainloop()

# this code below has better styling and colouring
import tkinter as tk

def convert():
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result_label.config(text=f"{cm:.2f} cm")
    except:
        result_label.config(text="Invalid input")

root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x400")
root.configure(bg="#f5f7fa")

title = tk.Label(root, text="Inches → Centimeters", font=("Arial", 18, "bold"), bg="#f5f7fa", fg="#333")
title.pack(pady=20)

frame = tk.Frame(root, bg="#f5f7fa")
frame.pack(pady=20)

entry = tk.Entry(frame, font=("Arial", 14), justify="center", bd=2, relief="groove")
entry.pack(ipady=5, pady=10)

convert_btn = tk.Button(root, text="Convert", font=("Arial", 12, "bold"),
                        bg="#4CAF50", fg="white", padx=20, pady=5,
                        command=convert, relief="flat")
convert_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 16), bg="#f5f7fa", fg="#222")
result_label.pack(pady=20)

footer = tk.Label(root, text="1 inch = 2.54 cm", font=("Arial", 10), bg="#f5f7fa", fg="gray")
footer.pack(side="bottom", pady=10)

root.mainloop()