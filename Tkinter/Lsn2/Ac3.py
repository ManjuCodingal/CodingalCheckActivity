#
from tkinter import *

# Setting up Main Window
root = Tk()
root.geometry("400x300")
root.title("main")

# Function to open New (Top Level) Window
def topwin():
    # Setting up Top Window
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    # Adding a label widget to Top Window
    l2 = Label(top, text="This is toplevel window")
    l2.pack()

# Adding a label and button Widget to Root (Main) Window
l = Label(root, text="This is root window")
btn = Button(root, text="Click here to open another window", command=topwin)
# command option:: In Tkinter, the command option is used to specify which function to run when the button is clicked.
# Whatever function you assign to command gets executed when the user presses the button

# Arranging widgets
l.pack()
btn.pack()

# Start the main event loop for the root window
root.mainloop()