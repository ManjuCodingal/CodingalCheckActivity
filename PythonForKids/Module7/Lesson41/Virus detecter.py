# Create a virus scanner simulation with pop-up alerts using Tkinter!
# 1) Import required modules:
#    a) Import everything from `tkinter` to create the GUI.
#    b) Import `messagebox` from `tkinter` to show popup alert messages.
from tkinter import *
from tkinter import messagebox

# 2) Create the main window using `root = Tk()`.
root=Tk()

# 3) Set the window size using `root.geometry("200x200")`.
root.geometry('200x200')

# 4) Define a function `msg()` to display a warning popup:
#    a) Use `messagebox.showwarning("Alert", "Stop! Virus Found.")`
#       to show a warning message box with a title and message.
#    b) This function will run when the button is clicked.
def msg():
    messagebox.showwarning("Alert","stop!Virus found!")


# 5) Create a Button widget:
#    a) Set the button text to "Scan for Virus".
#    b) Use `command=msg` so clicking the button calls the `msg()` function.
button=Button(root,text="Scan for virus",command=msg)

# 6) Place the button on the window using `button.place(x=40, y=80)`.
button.place(x=40,y=80)

# 7) Start the Tkinter event loop using `root.mainloop()`
#    so the window stays open and responds to user actions.
root.mainloop()