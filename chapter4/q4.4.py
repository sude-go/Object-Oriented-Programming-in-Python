"""
Write a program that draws an n-level staircase made of rectangles, such as
the example for n = 4 shown here.
"""
from cs1graphics import *

canvas = Canvas(400, 400)
canvas.setBackgroundColor("white")
rectangles = []

for i in range(1, 5):
    rect = Rectangle(20*i, 20)
    rect.setFillColor("gray")
    rect.setBorderColor("black")
    rect.moveTo(0, 20*(i-1))
    rectangles.append(rect)
    canvas.add(rect)
canvas.wait()

