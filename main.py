import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(5000)
bgcolor("black")
penup()  # Add this line to lift the pen before moving to the initial point
goto(hearta(0) * 20, heartb(0) * 20)  # Use heartb instead of hearta for y-coordinate
pendown()  # Add this line to put the pen down before drawing

for i in range(1, 6000):  # Start the loop from 1, not 0
    goto(hearta(i) * 20, heartb(i) * 20)  # Use heartb instead of hearta for y-coordinate
    for j in range(5):
        color("#f73487")
    goto(0, 0)  # Go back to the origin

done()
