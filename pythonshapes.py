from turtle import *
import math

# Name your Turtle.
mrTurtle = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
mrTurtle.setposition(x_pos, y_pos)

### Write your code below:

#user inputs
sidesString = input("Enter the number of sides: ")
sides = int(sidesString)
color = input("Enter the outside color you want: ")
fillColor = input("Enter the inside color you want: ")

#set colors
mrTurtle.pencolor(color)
mrTurtle.fillcolor(fillColor)

#begin fill and drawing
mrTurtle.begin_fill()
mrTurtle.pendown()

#create shape
for i in range(sides):
    mrTurtle.forward(100)
    mrTurtle.left(360/sides)
    
mrTurtle.penup()
mrTurtle.end_fill()


# Close window on click.
exitonclick()
