import turtle

# Constants
ANGLE = 60
LENGTH = 5

# Turtle setup
t = turtle.Turtle()
turtle.bgcolor("white")
turtle.title("Gosper Curve")
turtle.speed(0) # Maximum speed

# Translate the string into drawing instructions
for char in final_curve_string:
    if char == "A" or char == "B":
        t.forward(LENGTH)
    elif char == "-":
        t.left(ANGLE)
    elif char == "+":
        t.right(ANGLE)

# Keep the window open
turtle.done()