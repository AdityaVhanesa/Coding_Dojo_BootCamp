import unittest


def isPalindrom(array):
    length = len(array)
    middle = length // 2
    for i in range(middle):
        if array[i] != array[length - 1 - i]:
            return False

    return True


class IsPalindromTest(unittest.TestCase):
    def testOne(self):
        self.assertTrue(isPalindrom("racecar"))

    def testTwo(self):
        self.assertTrue(isPalindrom("madam"))

    def testThree(self):
        self.assertTrue(isPalindrom("civic"))

    def testFour(self):
        self.assertFalse(isPalindrom("Aditya"))

    def testFive(self):
        self.assertFalse(isPalindrom("False"))


if __name__ == '__main__':
    unittest.main()  # this runs our tests
