from math import gcd


class Fraction:
    def __init__(self, divided, sub):
        self.divided = divided
        self.sub = sub

        d = gcd(self.divided, self.sub)
        self.divided = self.divided // d
        self.sub = self.sub // d

    def __neg__(self):
        return Fraction(-self.divided, self.sub)

    def invert(self):
        return Fraction(self.sub, self.divided)

    def __str__(self):
        return f"{self.divided}/{self.sub}"


fraction = Fraction(7, 21)
negated_fraction = -fraction
inverted_fraction = fraction.invert()

print(f"Original Fraction: {fraction}")
print(f"Negated Fraction: {negated_fraction}")
print(f"inverted Fraction: {inverted_fraction}")
