# 1. Import Tkinter Module
# 2. Create the GUI (Graphical User Interface) application main Window
# 3. Add widgets

import tkinter as tk

# Create the GUI application main Window
window = tk.Tk()
window.title('Tkinter Sample Window')
window.geometry('300x300') # 'width x height'

# Label
greeting = tk.Label(text="Hello User", fg='black', bg='white')

# Button 
button = tk.Button(text="Click me", bg='black', fg='white')

# Entry 
entry = tk.Entry(fg="yellow", bg="blue", width=50)

# Pack widgets
greeting.pack()
button.pack()
entry.pack()

# Frame
frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
frame.pack()

# Label inside frame
label = tk.Label(master=frame, text='Sample Frame')
label.pack()

# Text widget inside frame
textbox = tk.Text(frame, fg='green', bg='yellow', height=5, width=30)
textbox.pack()

# Run the main event loop
window.mainloop()

