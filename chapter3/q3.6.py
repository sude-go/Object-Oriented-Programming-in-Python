"""
Only one rectangle appears? Why? How would you get two different rectangles to
show up? (There are several ways to fix this.)
"""

from cs1graphics import *

can = Canvas(200, 150)
rect = Rectangle()
rect.setWidth(50)
rect.setHeight(75)
rect.moveTo(25, 25)
can.add(rect)

rect = Rectangle()
rect.setWidth(100)
rect.setHeight(25)
can.add(rect)
# can.add(rect)  # add the same object twice to the canvas
