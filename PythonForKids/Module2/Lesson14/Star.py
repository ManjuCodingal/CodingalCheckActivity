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
board.right(150) # turns turtle 150 degrees to the clockwise. 150 is used to position the turtle for the second triangle of the star, which will be drawn on top of the first triangle. If we use 120 instead of 150, the second triangle will be drawn next to the first triangle instead of on top of it.
board.forward(50) # move turtle forward by 50 pixels. This is used to position the turtle for the second triangle of the star, which will be drawn on top of the first triangle. If we use 100 instead of 50, the second triangle will be drawn next to the first triangle instead of on top of it.
 
# second triangle for star
board.pendown() # Put down the pen to start drawing
board.right(90) # turns turtle 90 degrees to the clockwise
board.forward(100) # draw base
 
board.right(120) # turns turtle 120 degrees to the clockwise
board.forward(100) # draw second side of triangle
 
board.right(120) # turns turtle 120 degrees to the clockwise
board.forward(100) # draw third side of triangle
 
turtle.done() # Finish drawing and display the window