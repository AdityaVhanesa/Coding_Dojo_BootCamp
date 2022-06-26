import unittest


def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False


class IsEvenTests(unittest.TestCase):
    def testTwo(self):
        self.assertTrue(isEven(2))

    def testThree(self):
        self.assertFalse(isEven(3))

    def setUp(self) -> None:
        """ Running Setup before test"""
        print("Running Setup")

    def tearDown(self) -> None:
        print("Running Teardown Tasks")


if __name__ == '__main__':
    unittest.main()  # this runs our tests
