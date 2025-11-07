#William Davis
#10/31/2025
#Assignment: Shape Drawing with While Loops
#This program uses while loops to draw a square and a triangle using the turtle graphics library.

import turtle
win = turtle.Screen()  # Create a window for turtle graphics
# Create a turtle
t = turtle.Turtle()

# Add some display options
t.pensize(3)            # increase pensize (takes integer)
t.pencolor("Green")     # set pencolor (takes string)
t.shape("turtle")

# --- Draw a square using a while loop ---
sides = 0
while sides < 4:
    t.forward(100)   # move forward 100 units
    t.right(90)      # turn right 90 degrees
    sides += 1

# Move the turtle so shapes don't completely overlap
t.penup()
t.goto(-50, 0)
t.pendown()

# --- Draw a triangle using a while loop ---
sides = 0
while sides < 3:
    t.forward(100)   # move forward 100 units
    t.left(120)      # turn left 120 degrees
    sides += 1

