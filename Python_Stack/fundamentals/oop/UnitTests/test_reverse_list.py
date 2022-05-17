import unittest


def reverseList(array):
    length = len(array)
    middle = length // 2

    for i in range(middle):
        array[i], array[length - 1 - i] = array[length - 1 - i], array[i]
    return array


class IsReverseTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(reverseList([1, 2, 3]), [3, 2, 1])

    def testTwo(self):
        self.assertEqual(reverseList([]), [])

    def testThree(self):
        self.assertEqual(reverseList([1]), [1])

    def testFour(self):
        self.assertEqual(reverseList([1, 2, 3, 4]), [4,3,2,1])


if __name__ == '__main__':
    unittest.main()  # this runs our tests
