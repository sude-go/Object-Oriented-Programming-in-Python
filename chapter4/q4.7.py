from cs1graphics import *

levels = int(input("Enter the number of levels: "))
height = int(input("Enter the overall height of the pyramid: "))

canvas = Canvas(400, 400, "white", "Pyramid")

width = height * 2
size = width / levels

for i in range(levels):
    num_squares = levels - i
    y = height - size / 2 - i * size + 200

    for j in range(num_squares):
        x = size / 2 + j * size + i * size / 2 + 200
        square = Square(size, Point(x, y))
        square.setFillColor('blue')
        canvas.add(square)
