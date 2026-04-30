# Import tkinter
import tkinter as tk

# Function to calculate product
def calculate_product():
    try:
        # Get numbers from Entry boxes
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        # Calculate product
        product = num1 * num2

        # Display result in Text box
        result_box.delete("1.0", tk.END)   # Clear old result
        result_box.insert(tk.END, f"Product = {product}")

    except ValueError:
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, "Please enter valid numbers.")


# Create main window
window = tk.Tk()

# Set window size
window.geometry("400x300")

# Set window title
window.title("Getting Started with Widgets")

# Optional background color
window.configure(bg="#e6f2ff")


# Label describing functionality
desc_label = tk.Label(
    window,
    text="Enter two numbers to calculate their product.",
    bg="#e6f2ff",
    font=("Arial", 10)
)
desc_label.pack(pady=5)


# First number label
label1 = tk.Label(
    window,
    text="Enter First Number:",
    bg="#e6f2ff"
)
label1.pack()

# First Entry box
entry1 = tk.Entry(window, width=20)
entry1.pack(pady=5)


# Second number label
label2 = tk.Label(
    window,
    text="Enter Second Number:",
    bg="#e6f2ff"
)
label2.pack()

# Second Entry box
entry2 = tk.Entry(window, width=20)
entry2.pack(pady=5)


# Button to calculate product
calc_button = tk.Button(
    window,
    text="Calculate Product",
    command=calculate_product,
    bg="#4CAF50",
    fg="white"
)
calc_button.pack(pady=10)


# Text box to display result
result_box = tk.Text(
    window,
    height=2,
    width=30
)
result_box.pack(pady=5)


# Run the window
window.mainloop()