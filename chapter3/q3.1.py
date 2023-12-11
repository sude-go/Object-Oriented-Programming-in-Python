# The following code fragment has a single error in it. Fix it.
from cs1graphics import *

screen = Canvas()
disk = Circle()
disk.setFillColor('red')
# disk.add(screen)
# AttributeError: 'Circle' object has no attribute 'add'
screen.add(disk)
