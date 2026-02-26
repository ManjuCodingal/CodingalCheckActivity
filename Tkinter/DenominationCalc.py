from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Setting up Main Window
root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

# Adding Image and Labels in the Main Window
upload = Image.open("Tkinter/img.jpg") #("app_img.jpg")
# Resize the image using resize() method
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = Label(root,
               text="Hey User! Welcome to Denomination Counter Application.",
               bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER) #relx=0.5 === relative x-coordinate for the position of a widget, where relx=0.5 means the widget's horizontal position will be at 50% of the container's width. Essentially, it centers the widget horizontally within its parent container.

# Function to display a messagebox and proceed if OK is clicked
def msg():
    MsgBox = messagebox.showinfo(
        "Alert", "Do you want to calculate the denomination count?")
    if MsgBox == 'ok':
        topwin()

# Adding Buttons to the main window
button1 = Button(root,
                 text="Let's get started!",
                 command=msg,
                 bg='brown',
                 fg='white')
button1.place(x=260, y=360)

# Function for opening new/top window
def topwin():
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg='light grey')
    top.geometry("600x350+50+50")
#600x350 → Window Size
# 600: Width of the window in pixels.
# 350: Height of the window in pixels.
# So the window will be 600 pixels wide and 350 pixels tall.

# +50+50 → Window Position on Screen
# The first +50: Distance in pixels from the left edge of the screen.
# The second +50: Distance in pixels from the top edge of the screen.
# So the top-left corner of the window will appear:
# 50 pixels from the left, and
# 50 pixels from the top of your screen.
    label = Label(top, text="Enter total amount", bg='light grey')
    entry = Entry(top)
    lbl = Label(top, text="Here are number of notes for each denomination", bg='light grey')

    l1 = Label(top, text="2000", bg='light grey')
    l2 = Label(top, text="500", bg='light grey')
    l3 = Label(top, text="100", bg='light grey')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100

#             // (Floor Division Operator)
# What it does: It divides the number on the left by the number on the right, then rounds down to the nearest whole number (integer).
# It returns the quotient without the remainder.

# % (Modulo Operator)
# What it does: It calculates the remainder of the division of the number on the left by the number on the right.
# In other words, it tells you what’s left over after dividing.
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
#  t1.delete(0, END)            This deletes the current content of the Entry widget t1.
# 0: The start index, which indicates the first character (or position 0).
# END: This is a special constant in Tkinter that represents the last index of the text in the widget.
# Essentially, this removes all the text inside t1.

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    btn = Button(top, text='Calculate', command=calculator, bg='brown', fg='white')

    # Centering Widgets in the Top Window
    label.place(x=230, y=50   )
    entry.place(x=200, y=80   )
    btn.place(x=240, y=120   )
    lbl.place(x=140, y=170   )

    l1.place(x=180, y=200   )
    l2.place(x=180, y=230   )
    l3.place(x=180, y=260   )

    t1.place(x=270, y=200   )
    t2.place(x=270, y=230   )
    t3.place(x=270, y=260)

    top.mainloop()

root.mainloop()