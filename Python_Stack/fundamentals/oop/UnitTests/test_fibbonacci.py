import unittest


def fibonacci(number):
    previous_value_2 = 0
    previous_value_1 = 1
    current_value = 0
    if not number:
        return previous_value_2
    if number == 1:
        return previous_value_1

    for i in range(2, number + 1):
        current_value = previous_value_1 + previous_value_2
        previous_value_2 = previous_value_1
        previous_value_1 = current_value

    return current_value


class TestFibonacci(unittest.TestCase):
    def testOne(self):
        self.assertEqual(fibonacci(0), 0)

    def testTwo(self):
        self.assertEqual(fibonacci(1), 1)

    def testThree(self):
        self.assertEqual(fibonacci(5), 5)

    def testFour(self):
        self.assertEqual(fibonacci(8), 21)


if __name__ == '__main__':
    unittest.main()  # this runs our tests
