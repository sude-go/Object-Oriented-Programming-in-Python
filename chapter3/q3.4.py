"""
Assuming that you have already created an instance of the Square class
called sq, what’s wrong with the statement
sq.setFillColor(Red)
Give two different ways to fix this statement.
"""

from cs1graphics import *

screen = Canvas(200, 200)
sq = Square(100)
# sq.setFillColor(Red) # Error: Red is not defined
sq.setFillColor('Red')  # 1st way
sq.setFillColor('red')  # 2nd way
sq.moveTo(100, 100)
screen.add(sq)
