import turtle

turtle.Screen().bgcolor("Aqua")
board = turtle.Turtle()
 
# first triangle for star
board.forward(100) # draw base
 
board.left(120) # turns turtle 120 degrees to the counter-clockwise
board.forward(100) # draw second side of triangle
 
board.left(120) # turns turtle 120 degrees to the counter-clockwise
board.forward(100) # draw third side of triangle
 
board.penup() # Pick up the pen to move without drawing
board.right(150) # turns turtle 150 degrees to the clockwise
board.forward(50) # move turtle forward by 50 pixels
 
# second triangle for star
board.pendown() # Put down the pen to start drawing
board.right(90) # turns turtle 90 degrees to the clockwise
board.forward(100) # draw base
 
board.right(120) # turns turtle 120 degrees to the clockwise
board.forward(100) # draw second side of triangle
 
board.right(120) # turns turtle 120 degrees to the clockwise
board.forward(100) # draw third side of triangle
 
turtle.done() # Finish drawing and display the window