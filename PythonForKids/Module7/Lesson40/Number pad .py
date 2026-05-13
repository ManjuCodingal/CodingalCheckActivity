# Create a visual number pad interface using Tkinter! Students will learn to use nested loops, grid layout management, frames, and labels to build a phone-style number pad with organized rows and columns.
from tkinter import *

root=Tk()
root.title("Number pad")
root.geometry('250x300')

nums=[[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]

for i in range(4):
    root.rowconfigure(i,weight=1)
for j in range(3):
    root.columnconfigure(j,weight=1)

for i in range(4):
    for j in range(3):
        frame=Frame(root,relief=SUNKEN,borderwidth=1)
        frame.grid(row=i,column=j,sticky="nsew")
        label=Label(frame,text=nums[i][j],bg='white',font='TkDefaultFont')
        label.pack(padx=2,pady=2)
root.mainloop()
# 1) Import everything from `tkinter` to create the GUI.

# 2) Create the main window using `root = Tk()`.

# 3) Set the window title using `root.title('Number Pad')`
#    and set the window size using `root.geometry('250x300')`.

# 4) Create a 2D list `nums` that represents the number pad layout:
#    a) Each inner list represents one row of the keypad.
#    b) The layout includes numbers and special characters (# and *).

# 5) Use an outer loop to build 4 rows (i from 0 to 3):
#    a) Configure the root grid columns to resize nicely using `root.columnconfigure(...)`.
#    b) Configure the root grid rows to resize nicely using `root.rowconfigure(...)`.

# 6) Inside each row, use an inner loop to build 3 columns (j from 0 to 2):
#    a) Create a `Frame` for each keypad cell:
#       - Attach it to `root`
#       - Give it a sunken border style using `relief=SUNKEN`
#       - Set border thickness using `borderwidth=1`
#    b) Place the frame in the grid using `frame.grid(row=i, column=j)`.

# 7) Create a `Label` inside each frame:
#    a) Set label text as the corresponding value from `nums[i][j]`.
#    b) Set a background color for the label.
#    c) Pack the label inside the frame with padding.

# 8) Start the GUI event loop using `root.mainloop()`
#    so the window remains open and responds to user actions.