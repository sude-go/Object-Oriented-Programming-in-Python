from cs1graphics import *

canvas = Canvas(400, 400, 'white', 'Checkerboard')
layer = Layer()

colors = ['red', 'black']
for row in range(8):
    for col in range(8):
        square = Square(50, Point(col * 50 + 25, row * 50 + 25))
        square.setFillColor(colors[(row + col) % 2])
        layer.add(square)

piece_colors = ['white', 'black']
for row in range(3):
    for col in range(8):
        piece = Circle(20, Point(col * 50 + 25, row * 50 + 25))
        piece.setFillColor(piece_colors[row % 2])
        layer.add(piece)

for row in range(5, 8):
    for col in range(8):
        piece = Circle(20, Point(col * 50 + 25, row * 50 + 25))
        piece.setFillColor(piece_colors[row % 2])
        layer.add(piece)

canvas.add(layer)
