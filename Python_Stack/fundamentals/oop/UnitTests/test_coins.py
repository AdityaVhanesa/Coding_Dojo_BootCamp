import unittest


def changeCoins(cents):
    availableCoins = [25, 10, 5, 1]
    coinCounts = []
    for coin in availableCoins:
        coins_used = cents // coin
        cents = cents % coin
        coinCounts.append(coins_used)

    return coinCounts


class testChangeCoins(unittest.TestCase):
    def testOne(self):
        self.assertEqual(changeCoins(87), [3, 1, 0, 2])

    def testTwo(self):
        self.assertEqual(changeCoins(953), [38, 0, 0, 3])

    def testThree(self):
        self.assertEqual(changeCoins(1), [0, 0, 0, 1])

    def testFour(self):
        self.assertEqual(changeCoins(100), [4, 0, 0, 0])

    def testFive(self):
        self.assertEqual(changeCoins(1234), [49, 0, 1, 4])


if __name__ == '__main__':
    unittest.main()  # this runs our tests

