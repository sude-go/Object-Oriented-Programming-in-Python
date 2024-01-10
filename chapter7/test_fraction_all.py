import unittest
from chapter7.q7_6 import Fraction


class TestFraction(unittest.TestCase):
    def test_init(self):
        # Testing initializations
        f = Fraction()
        self.assertEqual(f._numer, 0)
        self.assertEqual(f._denom, 1)

        f = Fraction(3, 4)
        self.assertEqual(f._numer, 3)
        self.assertEqual(f._denom, 4)

        f = Fraction(-3, 4)
        self.assertEqual(f._numer, -3)
        self.assertEqual(f._denom, 4)

        f = Fraction(3, -4)
        self.assertEqual(f._numer, -3)
        self.assertEqual(f._denom, 4)

        f = Fraction(-3, -4)
        self.assertEqual(f._numer, 3)
        self.assertEqual(f._denom, 4)

        f = Fraction(0, 0)
        self.assertEqual(f._numer, 0)
        self.assertEqual(f._denom, 0)

    def test_add(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = f1 + f2
        self.assertEqual(f3._numer, 5)
        self.assertEqual(f3._denom, 4)

    def test_sub(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = f1 - f2
        self.assertEqual(f3._numer, 1)
        self.assertEqual(f3._denom, 4)

    def test_mul(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = f1 * f2
        self.assertEqual(f3._numer, 3)
        self.assertEqual(f3._denom, 8)

    def test_div(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = f2 / f1
        self.assertEqual(f3._numer, 2)
        self.assertEqual(f3._denom, 3)

    def test_lt(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 4)
        self.assertTrue(f2 < f1)

    def test_eq(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 4)
        f3 = Fraction(2, 4)
        self.assertTrue(f1 == f1)
        self.assertTrue(f1 != f2)
        self.assertTrue(f2 != f3)

    def test_float(self):
        f = Fraction(3, 4)
        self.assertEqual(float(f), 0.75)

    def test_int(self):
        f = Fraction(3, 4)
        self.assertEqual(int(f), 0)

    def test_str(self):
        f = Fraction(3, 4)
        self.assertEqual(str(f), '3/4')

        f = Fraction(0, 0)
        self.assertEqual(str(f), 'Undefined')


if __name__ == '__main__':
    unittest.main()
