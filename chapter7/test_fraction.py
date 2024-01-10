import unittest
from chapter7.q7_6 import Fraction


class TestFraction(unittest.TestCase):

    def test_add(self):
        # arrange
        f1 = Fraction(1, 2)  # create a fraction object with numerator 1 and denominator 2
        f2 = Fraction(2, 3)  # create another fraction object with numerator 2 and denominator 3

        # act
        f3 = f1 + f2  # use the __add__ method to add the two fractions

        # assert
        self.assertEqual(f3, Fraction(7,
                                      6))


if __name__ == '__main__':
    unittest.main()
