from math import sqrt


class Point:
    """
    The Point class represents a point in a 2D space. It stores the coordinates (x, y) of the point.
    The class provides methods for various operations like scaling, finding distance, normalizing, and mathematical operations.
    """

    def __init__(self, initialX=0, initialY=0):
        """
        Constructs a Point object.

        Parameters:
            initialX (int or float): The initial x-coordinate of the point. Default is 0.
            initialY (int or float): The initial y-coordinate of the point. Default is 0.
        """
        self._x = initialX
        self._y = initialY

    def getX(self):
        """
        Returns the x-coordinate of the point.

        Returns:
            int or float: The x-coordinate of the point.
        """
        return self._x

    def setX(self, val):
        """
        Sets the x-coordinate of the point.

        Parameters:
            val (int or float): The new x-coordinate of the point.
        """
        self._x = val

    def getY(self):
        """
        Returns the y-coordinate of the point.

        Returns:
            int or float: The y-coordinate of the point.
        """
        return self._y

    def setY(self, val):
        """
        Sets the y-coordinate of the point.

        Parameters:
            val (int or float): The new y-coordinate of the point.
        """
        self._y = val

    def scale(self, factor):
        """
        Scales the point by a given factor.

        Parameters:
            factor (int or float): The scaling factor.
        """
        self._x *= factor
        self._y *= factor

    def distance(self, other):
        """
        Calculates the Euclidean distance between this point and another point.

        Parameters:
            other (Point): The other point.

        Returns:
            float: The Euclidean distance between this point and the other point.
        """
        dx = self._x - other._x
        dy = self._y - other._y
        return sqrt(dx * dx + dy * dy)

    def normalize(self):
        """
        Normalizes the point, i.e., scales it such that its length (Euclidean distance from the origin) becomes 1.
        """
        mag = self.distance(Point())
        if mag > 0:
            self.scale(1 / mag)

    def __str__(self):
        """
        Returns a string representation of the point.

        Returns:
            str: The string representation of the point in the format '<x,y>'.
        """
        return '<' + str(self._x) + ',' + str(self._y) + '>'

    def __add__(self, other):
        """
        Adds this point to another point, returning a new point that is the sum of the two points.

        Parameters:
            other (Point): The other point.

        Returns:
            Point: The sum of this point and the other point.
        """
        return Point(self._x + other._x, self._y + other._y)

    def __mul__(self, operand):
        """
        Multiplies this point by a scalar or another point, returning a new point that is the product of the two.

        Parameters:
            operand (int, float, or Point): The scalar or other point to multiply this point by.

        Returns:
            Point: The product of this point and the scalar or other point.
        """
        if isinstance(operand, (int, float)):
            return Point(self._x * operand, self._y * operand)
        elif isinstance(operand, Point):
            return self._x * operand._x + self._y * operand._y
