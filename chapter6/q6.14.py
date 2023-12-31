from cs1graphics import *
from math import sqrt


class Point:
    def __init__(self, initial_x=0, initial_y=0, initial_z=0):
        self._x = initial_x
        self._y = initial_y
        self._z = initial_z

    def scale(self, factor):
        self._x *= factor
        self._y *= factor
        self._z *= factor

    def distance(self, other):
        dx = self._x - other._x
        dy = self._y - other._y
        dz = self._z - other._z
        return sqrt(dx * dx + dy * dy + dz * dz)

    def set_z(self, new_z):
        self._z = new_z

    def normalize_3d(self):
        mag = self.distance(Point())
        if mag > 0:
            self.scale(1 / mag)

    def __add__(self, other):
        return Point(self._x + other._x, self._y + other._y, self._z + other._z)

    def __str__(self):
        return '<' + str(self._x) + ',' + str(self._y) + ',' + str(self._z) + '>'


point1 = Point(1, 2, 3)
point2 = Point(4, 5, 6)

result_point = point1 + point2
print(result_point)

point1.scale(2)
print(point1)

distance_value = point1.distance(point2)
print(distance_value)

point2.normalize_3d()
print(point2)
