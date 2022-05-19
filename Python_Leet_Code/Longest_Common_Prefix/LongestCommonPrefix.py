import unittest


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
        self.numberOfChilds = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.commonPrefix = ""

    def insert(self, key):
        current_runner = self.root
        for value in key:
            if value not in current_runner.children:
                current_runner.children[value] = TrieNode()
                current_runner.numberOfChilds += 1
            if current_runner.numberOfChilds == 1 \
                    and not current_runner.isEndOfWord:
                self.commonPrefix += value
            else:
                return
            current_runner = current_runner.children[value]
        current_runner.isEndOfWord = True

    def searchCommonPrefix(self):
        current_runner = self.root
        commonPrefix = ""
        while current_runner.numberOfChilds == 1 and not current_runner.isEndOfWord:
            value, child = list(current_runner.children.items())[0]
            commonPrefix += value
            current_runner = child
        return commonPrefix


class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        T = Trie()
        for value in strs:
            if value == "" or len(value) == 0:
                return ""
            T.commonPrefix = ""
            T.insert(value)

        return T.commonPrefix


# solution = Solution()
# print(solution.longestCommonPrefix(["f", "fl", "flg"]))

class testSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def testOne(self):
        self.assertEqual(self.solution.longestCommonPrefix(["flower", "flow", "flight"]), "fl")

    def testTwo(self):
        self.assertEqual(self.solution.longestCommonPrefix(["dog", "racecar", "car"]), "")

    def testThree(self):
        self.assertEqual(self.solution.longestCommonPrefix(["a", "ab", "abcdefg"]), "a")


if __name__ == '__main__':
    unittest.main()  # this runs our tests
