import honeycomb

# Drawing the honeycomb pattern with default edge length
honeycomb.draw_honeycomb()

import turtle

myPen = turtle.Turtle()
myPen.shape("arrow")

myPen.color("#a86f14")
myPen.fillcolor("#efb456")
myPen.pensize(2)
myPen.speed(10) # Set the speed of the turtle

def drawCavity(x, y, edgeLength):
    myPen.penup()
    myPen.goto(x, y)
    myPen.pendown()
    myPen.begin_fill()
    for i in range(0, 6):
        myPen.forward(edgeLength)
        myPen.left(60)
    myPen.end_fill()

# Main Program Starts Here
for x in range(-150, 150, 60):
    drawCavity(x, 150, 20)

myPen.hideturtle()
turtle.done()

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import math

def draw_cavity(ax, x, y, edge_length):
    """Draws a hexagonal cavity at a given (x,y) position with specified edge length."""
    hexagon = patches.RegularPolygon((x, y), numVertices=6, radius=edge_length, orientation=np.pi/6, edgecolor="#a86f14", facecolor="#efb456")
    ax.add_patch(hexagon)

def draw_honeycomb(edge_length=20):
    """Draws the honeycomb pattern using hexagonal cavities."""
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.axis('equal')

    # Nested loops to arrange the hexagons in a 2D honeycomb pattern
    for x in range(-150, 150, 60):
        for y in range(-150, 150, int(60 * math.sqrt(3))):
            # Stagger every other row
            if (x//60) % 2 != 0:
                y += int(30 * math.sqrt(3))
            draw_cavity(ax, x, y, edge_length)

    plt.axis('off') # Turning off the axis
    plt.show()