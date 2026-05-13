from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry('200x200')
def msg():
    result=messagebox.askyesno("confirm","do u wnat to continue!")
    if result:
        print("User cliked yes")
    else:
        print("user clicked no !")
btn=Button(root,text="click me !",command=msg)
btn.pack()
root.mainloop()