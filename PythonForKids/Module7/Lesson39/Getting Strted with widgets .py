# 1) Import required libraries:
#    a) Import everything from `tkinter` to build the GUI.
#    b) Import `date` from `datetime` to display today’s date.
from tkinter import *
from datetime import date

# 2) Create the main window using `root = Tk()`.
root = Tk()

# 3) Set window properties:
#    a) Set the title using `root.title(...)`.
#    b) Set window size using `root.geometry(...)`.
root.title("Getting strated with widgets")
root.geometry("500x300")

# 4) Create the first label `lbl`:
#    a) Display text "Hey There!".
#    b) Set foreground (text) color, background color, height, and width.
lbl=Label(root,text="Hey there",fg='white',bg='blue',height=2,width=20)

# 5) Create a label `name_lbl` to ask the user for their full name.
name_lbl=Label(root,text='Enter your full name')


# 6) Create an Entry widget `name_entry`:
#    a) This provides a text box for the user to type their name.
text_box=Text(root,height=8,width=40)
name_entry=Entry(root,width=30)

# 7) Define a function `display()` that runs when the button is clicked:
#    a) Read the user’s input from the entry box using `name_entry.get()`.
#    b) Create a greeting message using the entered name.
#    c) Create a message string that includes a welcome text and the date heading.
#    d) Use a global variable `message` so it can be accessed anywhere if needed.
#    e) Insert the greeting, message, and today’s date into the text box using `text_box.insert(...)`.
def display():
    global message
    name=name_entry.get()
    greeting='Hello'+name+'!'
    message="\nWelcome to tkinter.\nToday's date is :\n"
    today=date.today()
    text_box.insert(END,greeting+'\n')
    text_box.insert(END,message)
    text_box.insert(END,today)

# 8) Create a Text widget `text_box`:
#    a) This is used to display output messages inside the GUI.


# 9) Create a Button widget `btn`:
#    a) Set button text to "Begin".
#    b) Set `command=display` so clicking the button calls the `display()` function.
#    c) Set height, background color, and text color.
btn=Button(root,text='Begin',command=display,height=2,bg='green',fg='white')
# 10) Arrange all widgets in the window using `pack()`:
#     a) Pack the main label.
#     b) Pack the name label.
#     c) Pack the name entry box.
#     d) Pack the button.
#     e) Pack the text box.
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

# 11) Start the GUI event loop using `root.mainloop()`
#     so the window stays open and responds to user actions.
root.mainloop()