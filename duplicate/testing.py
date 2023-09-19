import unittest

from solution import Solution

class Testing(unittest.TestCase):
    def test_one(self):
        self.assertEqual(Solution().duplicate([1,2,3,1]), 1);
    def test_two(self):
        self.assertEqual(Solution().duplicate([1,2,3,2]), 2);
    def test_three(self):
        self.assertEqual(Solution().duplicate([1,1,1,3,3,4,3,2,4,2]), 1);
    def test_four(self):
        self.assertEqual(Solution().duplicate([11,2,13,4,5,6,7,8,9,10,9,3,12,13,14]), 13);

if __name__ == '__main__':
    unittest.main()