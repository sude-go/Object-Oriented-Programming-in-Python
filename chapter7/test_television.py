import unittest
from chapter7.q7_3 import Television


class TestTelevision(unittest.TestCase):
    def setUp(self):
        self.television = Television()

    def test_togglePower(self):
        self.assertTrue(self.television.togglePower())

    def test_channelUp(self):
        self.assertEqual(self.television.channelUp(), 2)

    def test_channelDown(self):
        self.assertEqual(self.television.channelDown(), 1)

    def test_setChannel(self):
        self.assertEqual(self.television.setChannel(10), 10)

    def test_volumeUp(self):
        self.assertEqual(self.television.volumeUp(), 6)

    def test_volumeDown(self):
        self.assertEqual(self.television.volumeDown(), 5)

    def test_toggleMute(self):
        self.assertTrue(self.television.toggleMute())

    def test_jumpPrevChannel(self):
        self.assertEqual(self.television.jumpPrevChannel(), 99)


if __name__ == '__main__':
    unittest.main()
