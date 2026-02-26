# Make sure you upload image in your current Repl
# Import all the necessary libraries
# PIL (Python Imaging Library) provides image editing capabilities to the python interpreter 

#  do  pip install Pillow if pip error

from tkinter import *
from PIL import Image, ImageTk

# Create a window with a title bar and set its geometry as well
root = Tk()
root.title('image')
root.geometry('400x400')

# Now use Image.open to open and identify the given image file. 
# upload = Image.open("img.jpg")
upload = Image.open("Tkinter/Lsn2/img.jpg")

# Convert this Image to Tkinter compatible image
image = ImageTk.PhotoImage(upload)

# Add image to Tkinter Label
label = Label(root, image=image, height=350, width=300)
label.place(x=50, y=0)
label2 = Label(root, text="This is how you add image in Tkinter Window")
label2.place(x=40, y=360)

# Run the application
root.mainloop()