class Fraction:
    def __init__(self, divided, sub):
        self.divided = divided
        self.sub = sub

    def __neg__(self):
        return Fraction(-self.divided, self.sub)

    def __str__(self):
        return f"{self.divided}/{self.sub}"


fraction = Fraction(3, 4)
negated_fraction = -fraction

print(f"Original Fraction: {fraction}")
print(f"Negated Fraction: {negated_fraction}")
