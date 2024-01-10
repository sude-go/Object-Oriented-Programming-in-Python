import unittest


class TestTextInput(unittest.TestCase):
    def test_unique_leading_chars(self):
        colorNames = ["red", "blue", "green"]
        uniqueChars = set()
        for colorName in colorNames:
            leadingChar = colorName[0]
            self.assertNotIn(leadingChar, uniqueChars)
            uniqueChars.add(leadingChar)
