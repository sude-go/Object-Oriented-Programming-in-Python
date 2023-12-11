"""
Assuming that you have already successfully created a Canvas instance
called can, you enter the following to draw a blue circle centered in a red square.
But the circle never appears. What’s wrong with the above program? Edit the program so it works as desired.
"""

from cs1graphics import *

can = Canvas()  # create a canvas object

# following code:
sq = Square()
sq.setSize(40)
sq.moveTo(50, 50)
sq.setFillColor('Red')
can.add(sq)

cir = Circle()
cir.moveTo(50, 50)
cir.setRadius(15)
cir.setFillColor('Blue')
can.add(cir)
