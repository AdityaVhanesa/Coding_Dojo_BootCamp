import unittest

from mathDojo import MathDojo


class TestMathDojo(unittest.TestCase):

    def setUp(self) -> None:
        self.dojo = MathDojo()

    def testOne(self):
        self.assertEqual(self.dojo.add(1).result, 1)

    def testTwo(self):
        self.dojo.result = 0
        self.assertEqual(self.dojo.add(1, 1, 1, 1, 1, 1, 1, 1).result, 8)

    def testThree(self):
        self.dojo.result = 50
        self.assertEqual(self.dojo.subtract(1).result, 49)

    def testFour(self):
        self.dojo.result  = 8
        self.assertEqual(self.dojo.subtract(2, 2, 2).result, 2)


if __name__ == '__main__':
    unittest.main()  # this runs our tests
