# Write a Python program to create a Denominator Calculator to calculate the number of notes of denominations - 2000, 500, and 100 for the amount entered by the user
# 1) Import required libraries:
#    a) Import everything from `tkinter` to build the GUI.
#    b) Import `messagebox` from tkinter to show popup messages.
#    c) Import `Image` and `ImageTk` from PIL to load and display images.
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# 2) Create the main window using `root = Tk()`.
root=Tk()

# 3) Set main window properties:
#    a) Set title as "Denomination Counter".
#    b) Set background color to "light blue".
#    c) Set window size to 650x400.
root.title("Denomination calculator")
root.config(bg="light blue")
root.geometry("650x400")
# 4) Load and display an image on the main window:
#    a) Open the image file "app_img.jpg" using `Image.open()`.
#    b) Resize the image to (300, 300).
#    c) Convert the image to a Tkinter compatible format using `ImageTk.PhotoImage()`.
#    d) Create a Label widget with the image and place it on the window.
img=Image.open("denomCalc.jpg")
img=img.resize((300,300))
photo=ImageTk.PhotoImage(img)
img_label=Label(root,image=photo,bg="light blue")
img_label.place(x=180,y=20)
 

# 5) Add a welcome label (`label1`) below the image with a greeting message.
label1=Label(root,text="Welcome to denomination calculator",bg="light blue",font=("Arial",14))
label1.place(x=180,y=5)

# 6) Define a function `msg()` to show a confirmation messagebox:
#    a) Use `messagebox.showinfo()` to ask the user if they want to calculate denominations.
#    b) If the user clicks "ok", call `topwin()` to open the calculator window.
def msg():
    msgbox=messagebox.askyesno("Information","Do you want to calculate denominations ?")
    if msgbox==True:
        topwin()

# 7) Create a button `button1` on the main window:
#    a) Set its text to "Let's get started!".
#    b) Set `command=msg` so clicking the button calls the `msg()` function.
#    c) Set button background and text color.
#    d) Place the button at the bottom.
button1=Button(root,text="Lets get started",command=msg,bg="blue",fg="white")
button1.place(x=260,y=360)

# 8) Define a function `topwin()` to open a new (top-level) window:
#    a) Create a new window using `top = Toplevel()`.
#    b) Set its title, background color, and size.
def topwin():
    top=Toplevel()
    top.title('Calculator')
    top.config(bg="white")
    top.geometry("500x400")

# 9) Add input widgets in the top window:
#    a) Create a label asking the user to "Enter total amount".
#    b) Create an Entry box `entry` for the user to type the amount.
    label=Label(top,text="Enter total amount",bg="white")
    label.place(x=230,y=50)
    entry=Entry(top)
    entry.place(x=200,y=80)

# 10) Add labels and entry boxes to show denomination note counts:
#     a) Create a heading label describing the output.
#     b) Create labels for denominations: 2000, 500, and 100.
#     c) Create three entry boxes (`t1`, `t2`, `t3`) to display results.
    heading=Label(top,text="number of notes",bg="white",font=("Arial",12))
    heading.place(x=140,y=170)
    L1=Label(top,text="2000",bg="white")
    L1.place(x=180,y=200)
    L2=Label(top,text="500",bg="white")
    L2.place(x=180,y=240)
    L3=Label(top,text="100",bg="white")
    L3.place(x=180,y=280)

    t1=Entry(top)
    t1.place(x=270,y=200)
    t2=Entry(top)
    t2.place(x=270,y=240)
    t3=Entry(top)
    t3.place(x=270,y=280)

# 11) Define a nested function `calculator()` inside `topwin()`:
#     a) Try to convert the entered amount to an integer.
#     b) Calculate number of 2000 notes using integer division (`//`) and update remaining amount using `%`.
#     c) Calculate number of 500 notes similarly.
#     d) Calculate number of 100 notes similarly.
#     e) Clear previous values in output entry boxes using `delete()`.
#     f) Insert the calculated note counts into `t1`, `t2`, and `t3`.
#     g) If input is invalid, show an error popup using `messagebox.showerror()`.
    def calculator():
        try:
            amount=int(entry.get())
            note2000=amount//2000
            amount=amount%2000

            note500=amount//500
            amount=amount%500

            note100=amount//100
            amount=amount%100

            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)

            t1.insert(END,str(note2000))
            t2.insert(END,str(note500))
            t3.insert(END,str(note100))
        except:
            messagebox.showerror("Error","Invalid input")

# 12) Create a "Calculate" button in the top window:
    btn=Button(top,text="calculate",command=calculator)
    btn.place(x=240,y=120)
#     a) Set `command=calculator` so clicking it performs the calculation.

# 13) Place all widgets in the top window using `.place()` at fixed coordinates.

# 14) Start the event loop for the top window using `top.mainloop()`.
    # top.mainloop()

# 15) Start the main GUI event loop using `root.mainloop()`
#     so the main window stays open and responds to user actions.
root.mainloop()