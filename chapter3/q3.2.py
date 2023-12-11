# Write a program that draws a filled triangle near the middle of a canvas.
from cs1graphics import *

screen = Canvas(200, 200)
triangle = Polygon(Point(100, 100), Point(200, 100), Point(150, 200))
triangle.setFillColor('red')
triangle.moveTo(50, 50)
screen.add(triangle)
