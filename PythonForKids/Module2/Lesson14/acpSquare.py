import turtle

# Create screen
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Beautiful Square")

# Create turtle
pen = turtle.Turtle()
pen.pensize(5)
pen.speed(3)

# Colours for each side
colors = ["red", "blue", "green", "purple"]

# Draw square
for i in range(4):
    pen.color(colors[i])
    pen.forward(150)
    pen.right(90)

turtle.done()