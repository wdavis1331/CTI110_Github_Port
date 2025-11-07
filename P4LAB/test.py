import turtle

# Create turtle
t = turtle.Turtle()
t.pensize(8)
t.pencolor("blue")
t.speed(5)

# --- Draw first initial: W ---
t.penup()
t.goto(-150, 0)  # start on the left
t.pendown()

t.right(90)
t.forward(150)        # left vertical line

t.right(-120)
t.forward(90)         # up to middle

t.right(60)
t.forward(90)         # down to middle

t.left(120)
t.forward(150)        # right vertical line of W

# --- Move to position for D ---
t.penup()
t.goto(50, 0)
t.setheading(90)      # face upward for D
t.pendown()

# --- Draw second initial: D ---
t.forward(-150)        # vertical line
t.right(90)
t.circle(75, 180)    # outer curve of D

# Hide turtle
t.hideturtle()
turtle.done()
