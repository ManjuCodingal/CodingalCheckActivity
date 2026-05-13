# 1) Import everything from `tkinter` to create the GUI.
from tkinter import * 

# 2) Create the main window using `root = Tk()`.
root=Tk()

# 3) Set main window properties:
#    a) Set window size using `root.geometry("400x300")`.
#    b) Set window title using `root.title("main")`.
root.geometry("400x300")
root.title("main")

# 4) Define a function `topwin()` to open a new top-level window.


# 5) Inside `topwin()`:
#    a) Create a new window using `top = Toplevel()`.
#       (This creates a child window on top of the main window.)
#    b) Set the new window size using `top.geometry("180x100")`.
#    c) Set the new window title using `top.title("toplevel")`.
def topwin():
    top=Toplevel()
    top.geometry("180x180")
    top.title("Top level ")


# 6) Add a label widget to the top-level window:
#    a) Create `l2 = Label(top, text="This is toplevel window")`.
#    b) Display it using `l2.pack()`.
    Label2=Label(top,text="This is a toplevel window ")
    Label2.pack()

# 7) Start the event loop for the top window using `top.mainloop()`.
#    (This keeps the top window active.)
    top.mainloop()

# 8) Create widgets in the main window:
#    a) Create a label `l` with text "This is root window".
#    b) Create a button `btn` with text "click here to open another window".
#       Set `command=topwin` so clicking the button opens the new window.
label=Label(root,text="this is root window .")
label.pack()
btn=Button(root,text="click here to open the top window",command=topwin)

# 9) Arrange the main window widgets using `pack()`:
#    a) Pack the label.
#    b) Pack the button.
btn.pack()

# 10) Start the main GUI event loop using `root.mainloop()`
#     so the main window stays open and responds to user actions.
root.mainloop()