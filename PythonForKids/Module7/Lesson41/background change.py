# from tkinter import *
# root=Tk()
# root.geometry('200x200')
# def change_background():
#     root.configure(bg='lightblue')
# def change_color_green():
#     root.configure(bg='green')
# btn=Button(root,text='change color',command=change_background)
# btn.pack()
# btn2=Button(root,text='change color',command=change_color_green)
# btn2.pack()
# root.mainloop()
from tkinter import *
root=Tk()
root.geometry('200x200')
def change_background(color):
    root.configure(bg=color)

btn=Button(root,text='change color',command=lambda:change_background('lightblue'))# lambda is used to pass arguements.
btn.pack()
btn2=Button(root,text='change color',command=lambda:change_background('green'))
btn2.pack()
root.mainloop()