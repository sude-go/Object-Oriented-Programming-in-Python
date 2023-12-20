"""
Write a short program that uses a for loop to animate a circle moving across
a canvas.
"""
from cs1graphics import *
import time

can = Canvas(400, 400)
can.setBackgroundColor('black')

cir = Circle(20, Point(0, 200))
cir.setFillColor('red')
can.add(cir)

can.refresh()

while True:
    # Move the circle across the canvas
    for i in range(400):
        cir.move(1, 0)
        can.refresh()
        time.sleep(.01)

    # Move the circle back to the left
    for i in range(400):
        cir.move(-1, 0)
        can.refresh()
        time.sleep(.01)
