import unittest
from chapter7.q7_6 import Fraction as Fraction1
from chapter7.q7_9 import Fraction as Fraction2


class TestFraction(unittest.TestCase):
    def test_int(self):
        f1 = Fraction1(3, 4)
        f2 = Fraction2(3, 4)
        self.assertEqual(int(f1), int(f2))
