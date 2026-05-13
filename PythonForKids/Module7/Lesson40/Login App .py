# Create a user registration form with Tkinter! Students will learn to build a login interface with text input fields, password masking, button functionality, and message display. Perfect for understanding form creation and user interaction in GUI applications.
from tkinter import *

root=Tk()
root.title("Login App")
root.geometry("400x400")

frame=Frame(root,width=300,height=250,bg='white')
frame.place(x=50,y=20)

name_label=Label(frame,text="full name",bg= '#27A9F5',fg='black',width=15)
email_label=Label(frame,text='Email ID',bg='#27A9F5',fg='black',width=15)
pass_label=Label(frame,text='password',bg='#27A9F5',fg='black',width=15)

name_entry=Entry(frame)
email_entry=Entry(frame)
pass_entry=Entry(frame,show='*')

def display():
    name=name_entry.get()
    greeting= f'Hello {name} !\n'
    message='Your account is created'

    textbox.insert(END,greeting)
    textbox.insert(END,message)

textbox=Text(root,height=5,width=40)
btn=Button(frame,text='create account',bg='green',fg='white',command=display)

name_label.place(x=10,y=20)
name_entry.place(x=150,y=20)

email_label.place(x=10,y=60)
email_entry.place(x=150,y=60)

pass_label.place(x=10,y=100)
pass_entry.place(x=150,y=100)

btn.place(x=100,y=150)

textbox.place(x=40,y=300)

frame.place(x=40,y=0)

root.mainloop()

# 1) Import everything from `tkinter` to build the GUI.

# 2) Create the main window using `root = Tk()`.

# 3) Set window properties:
#    a) Set the title to "Login App".
#    b) Set the window size to 400x400.

# 4) Create a `Frame` widget to organize the form elements:
#    a) Attach the frame to `root`.
#    b) Set height, width, and background color.

# 5) Create three labels inside the frame:
#    a) Label for Full Name.
#    b) Label for Email Id.
#    c) Label for Password.
#    (Set background color, text color, and width for each label.)

# 6) Create Entry widgets inside the frame for user input:
#    a) `name_entry` for full name input.
#    b) `email_entry` for email input.
#    c) `pass_entry` for password input with hidden characters using `show="*"`.

# 7) Define a function `display()` that runs when the button is clicked:
#    a) Get the entered name using `name_entry.get()`.
#    b) Create a greeting message using the name.
#    c) Create a confirmation message for account creation.
#    d) Insert the greeting and message into the `textbox` using `textbox.insert(...)`.

# 8) Create a `Text` widget named `textbox` to display output messages.

# 9) Create a Button widget `btn`:
#    a) Set text to "Create Account".
#    b) Set `command=display` so clicking the button calls the `display()` function.
#    c) Set the button background color.

# 10) Arrange all widgets using `place()`:
#     a) Place the frame on the window.
#     b) Place each label and its corresponding entry box.
#     c) Place the button below the input fields.
#     d) Place the textbox at the bottom to show messages.

# 11) Start the GUI event loop using `root.mainloop()`
#     so the window stays open and responds to user actions.