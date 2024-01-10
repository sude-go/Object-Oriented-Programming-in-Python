import unittest
from chapter7.q7_11 import Date


class TestDate(unittest.TestCase):

    def test_computeNext(self):
        # Regular year
        date = Date(12, 31, 2021)
        next_date = date.computeNext()
        self.assertEqual(next_date.month, 1)
        self.assertEqual(next_date.day, 1)
        self.assertEqual(next_date.year, 2022)

        # Leap year
        date = Date(12, 31, 2020)
        next_date = date.computeNext()
        self.assertEqual(next_date.month, 1)
        self.assertEqual(next_date.day, 1)
        self.assertEqual(next_date.year, 2021)

        # February 28 in a non-leap year
        date = Date(2, 28, 2022)
        next_date = date.computeNext()
        self.assertEqual(next_date.month, 3)
        self.assertEqual(next_date.day, 1)
        self.assertEqual(next_date.year, 2022)


if __name__ == '__main__':
    unittest.main()
