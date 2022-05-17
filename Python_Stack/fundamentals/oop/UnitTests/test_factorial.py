import unittest


def factorial(number):
    value = 1
    for i in range(number, 1, -1):
        value *= i

    return value


class TestFactorial(unittest.TestCase):
    def testOne(self):
        self.assertEqual(factorial(5), 120)

    def testTwo(self):
        self.assertEqual(factorial(0), 1)

    def testThree(self):
        self.assertEqual(factorial(1), 1)


if __name__ == '__main__':
    unittest.main()  # this runs our tests
