# 1) Import everything from `tkinter` to create the GUI.
from tkinter import *

# 2) Create the main window using `window = Tk()`.
window=Tk()

# 3) Set window properties:
#    a) Set the title to "Event Handler".
#    b) Set the window size to 100x100.
window.title("Event handler")
window.geometry('100x100')

# 4) Define a function `handle_keypress(event)` to handle keyboard events:
#    a) This function receives an `event` object automatically.
#    b) Print `event.char` to show which key/character was pressed.
def handle_keypress(event):
    print('Key pressed',event.char)

# 5) Bind the keypress event to the window:
#    a) Use `window.bind("<Key>", handle_keypress)` so every key press triggers the function.
window.bind("<Key>",handle_keypress)

# 6) Define a function `handle_click(event)` to handle button click events:
#    a) This function also receives an `event` object automatically.
#    b) Print a message when the button is clicked.
def handle_click(event):
    print("Button clciked")
# 7) Create a Button widget with the text "Click me!" and display it using `pack()`.
button=Button(window,text='Click me !')
button.pack()

# 8) Bind the left mouse click event to the button:
#    a) Use `button.bind("<Button-1>", handle_click)` so left-click triggers the function.
button.bind("<Button-1>",handle_click)

# 9) Start the GUI event loop using `window.mainloop()`
#    so the window stays open and responds to user actions.
window.mainloop()