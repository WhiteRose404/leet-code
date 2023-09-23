import unittest 
import random

from solution import Solution

class Testing(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().shortest([[1,2,3],[0],[0],[0]]), 4);
    def test2(self):
        self.assertEqual(Solution().shortest([[1],[0,2,4],[1,3,4],[2],[1,2]]), 4);
    def test3(self):
        self.assertEqual(Solution().shortest([[1],[0,2,4],[1,3],[2],[1]]), 4);

if __name__ == '__main__':
    unittest.main()
    