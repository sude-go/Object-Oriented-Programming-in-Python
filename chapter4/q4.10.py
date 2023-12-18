"""
Write a program that draws an n-level staircase made of squares, such as
the example for n = 4 shown here.
"""
from cs1graphics import *

n = int(input("Enter the number of levels: "))
canvas = Canvas(400, 400, "white", "Staircase")
size = 20

for i in range(n):
    for j in range(i + 1):
        x = size / 2 + j * size + 200
        y = 200 - size / 2 + i * size
        square = Square(size, Point(x, y))
        square.setFillColor('blue')
        canvas.add(square)
