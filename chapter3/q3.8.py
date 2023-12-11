"""
Use the Layer class of the graphics library to create a pine tree. Make copies
of the tree and use it to draw a forest of pine trees.
"""

from cs1graphics import *

can = Canvas(500, 500)
can.setBackgroundColor('skyBlue')
can.setTitle('Pine Tree Forest')

lay = Layer()
can.add(lay)

# tree trunk
for i in range(10):
    trunk = Rectangle(5, 50)
    trunk.setFillColor('brown')
    trunk.setBorderColor('brown')
    trunk.moveTo(50 + i * 50, 50)
    lay.add(trunk)

# tree leaves
for i in range(10):
    leaves = Polygon(Point(50 + i * 50, 0), Point(25 + i * 50, 50), Point(75 + i * 50, 50))  # triangle
    leaves.setFillColor('green')
    leaves.setBorderColor('green')
    lay.add(leaves)

# forest
for i in range(10):
    lay2 = Layer()
    lay2.add(lay)
    lay2.moveTo(0, 75 + i * 75)
    can.add(lay2)


