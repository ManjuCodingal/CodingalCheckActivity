import turtle     #importing library       
my_wn = turtle.Screen()
my_wn.bgcolor("light blue") #screen background color
my_wn.title("Turtle")
my_pen = turtle.Turtle()
size = 0 # initial size of the spiral, it will be increased in the loop to create spiral effect
while True: #iterate loop
# while size > -100:   # stop when size becomes -100. Size is decreased by 5 pixels in each iteration, so it will stop after 20 iterations (0, -5, -10, ..., -95)
  for i in range(4): 
    my_pen.fd(size + 1) # fd is forward, size is increased by 1 pixel
    my_pen.left(90) # turns turtle 90 degrees to the left
    size = size - 5 # size is decreased by 5 pixels to create spiral effect., can check with 50 instead of 5 as well
  size = size + 1 # size is increased by 1 pixel to create spiral effect