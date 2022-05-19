import unittest


class Solution:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x = x // 10

        return x == revertedNumber or x == revertedNumber // 10


class testSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def testOne(self):
        self.assertFalse(self.solution.isPalindrome(-121))

    # def testTwo(self):
    #     self.assertFalse(self.solution.isPalindrome(1000))
    #
    # def testThree(self):
    #     self.assertTrue(self.solution.isPalindrome(1234321))
    #
    # def testFour(self):
    #     self.assertTrue(self.solution.isPalindrome(1))
