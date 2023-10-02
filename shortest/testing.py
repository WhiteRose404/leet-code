import unittest
from solution import Solution

class Testing(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().shortest([[1,2],[3,2],[0,1]]), -1);
    def test2(self):
        self.assertEqual(Solution().shortest([[0,1],[0,2],[1,3],[2,1]]), 3);
    def test3(self):
        self.assertEqual(Solution().shortest([[0,1],[0,2],[1,3]]), -1);
    def test4(self):
        self.assertEqual(Solution().shortest([[0,1],[1,2],[2,3],[3,4],[4,0]]), 5);

    # add random cases
if __name__ == '__main__':
    unittest.main()
    