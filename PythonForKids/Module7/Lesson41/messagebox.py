from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry('200x200')
def msg():
    messagebox.showinfo("Title","This is a sample message")
btn=Button(root,text='click me',command=msg)
btn.pack()
root.mainloop()