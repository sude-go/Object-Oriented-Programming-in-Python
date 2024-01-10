from chapter5.q5_19 import gcd


class Fraction:
    def __init__(self, numerator=0, denominator=1):
        """
         Initializes a new Fraction object with the specified numerator
         and denominator. If no arguments are provided,
         the default fraction is 0/1. The method also includes
         error handling for fractions that are undefined (denominator is 0).
        """
        if denominator == 0:  # fraction is undefined
            self._numer = 0
            self._denom = 0
        else:
            factor = gcd(abs(numerator), abs(denominator))
            if denominator < 0:  # want to divide through by negated factor
                factor = -factor
                self._numer = numerator // factor
                self._denom = denominator // factor

    def __add__(self, other):
        """"
         Adds the current fraction to another fraction.
         This method is equivalent to finding the least common multiple
         of the denominators, then adding the fractions using that common multiple.
         """
        return Fraction(self._numer * other._denom + self._denom * other._numer,
                        self._denom * other._denom)

    def __sub__(self, other):
        """
         Subtracts another fraction from the current fraction.
         This method is equivalent to adding the negation of the other fraction.
        """
        return Fraction(self._numer * other._denom - self._denom * other._numer,
                        self._denom * other._denom)

    def __mul__(self, other):
        """
        Multiplies the current fraction by another fraction.
        This method is equivalent to multiplying the numerators and the denominators separately.
        """
        return Fraction(self._numer * other._numer, self._denom * other._denom)

    def __div__(self, other):
        """
        Divides the current fraction by another fraction.
        This method is equivalent to multiplying the current fraction by the reciprocal of the other fraction.
        :param other:
        :return:
        """
        return Fraction(self._numer * other._denom, self._denom * other._numer)

    def __lt__(self, other):
        """
        Compares the current fraction to another fraction.
        The current fraction is considered less than the other fraction
        if the numerator of the current fraction multiplied by the
        denominator of the other fraction is less than the numerator
        of the other fraction multiplied by the denominator of the current fraction.
        """
        return self._numer * other._denom < self._denom * other._numer

    def __eq__(self, other):
        """
        Checks if the current fraction is equal to another fraction.
        Two fractions are considered equal if their numerators and denominators are equal.
        """
        return self._numer == other._numer and self._denom == other._denom

    def __float__(self):
        """
        Converts the current fraction to a floating-point number.
        This method is equivalent to dividing the numerator by the denominator.
        """
        return float(self._numer) / self._denom

    def __int__(self):
        """
        Converts the current fraction to an integer by truncating the decimal part of the floating-point number.
        This method first converts the fraction to a floating-point number,
        then truncates the decimal part by removing all digits after the decimal point.
        """
        return int(float(self))

    def __str__(self):
        """
        Returns a string that represents the current fraction.
         If the denominator is 0, the fraction is undefined and the string is 'Undefined'.
         If the denominator is 1, the fraction is a whole number and the string is the numerator.
         Otherwise, the string is the numerator followed by a slash and the denominator.
        """
        if self._denom == 0:
            return 'Undefined'
        elif self._denom == 1:
            return str(self._numer)
        else:
            return str(self._numer) + '/' + str(self._denom)
