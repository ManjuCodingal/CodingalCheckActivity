# Import necessary libraries
from tkinter import *
from tkinter import messagebox

# Setup Tkinter Window
root = Tk()
root.geometry("200x200")

# Function for Displaying Warning Message
# This will be called once the button is clicked
# messagebox.showwarning("Window Name", "Text to be displayed")
def msg():
	messagebox.showwarning("Alert", "Stop! Virus Found.")

# Adding Button Widget to Window
button = Button(root, text="Scan for Virus", command=msg)  # Create a Button inside the root window
button.place(x=40, y=80)
# After creating a widget, you must tell Tkinter where to put it.
# place() is one of Tkinter’s geometry managers (others are pack() and grid()).
# How place() works:
# It positions the widget at an exact coordinate (x, y) inside the parent (root window here).
# (0, 0) would be the top-left corner.
# (40, 80) means 40 pixels right and 80 pixels down from the top-left corner.

# place()
# Positions widgets at exact x, y coordinates.
# Example:
# button.place(x=40, y=80)
# → Button is fixed at 40px from left, 80px from top.
# ✅ Good for precise positioning (like a canvas or custom layout).

# pack()
# Automatically arranges widgets relative to each other.
# By default, it stacks widgets top to bottom.
# You can also pack them to the left, right, or bottom.

# Entering main event loop
root.mainloop()