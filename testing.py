import unittest

from solution import Solution

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().candy([1,0,2]), 5);

    def test2(self):
        self.assertEqual(Solution().candy([1,2,2]), 4);

    def test3(self):
        self.assertEqual(Solution().candy([1,3,2,2,1]), 7);

    def test4(self):
        self.assertEqual(Solution().candy([1,3,4,5,2]), 11);

    def test5(self):
        self.assertEqual(Solution().candy([1,2,3,4,7,6,5,4,3,2,1]), 38);

    def test6(self):
        self.assertEqual(Solution().candy([1,6,10,8,7,3,2]), 18);

    def test6(self):
        self.assertEqual(Solution().candy([5,3,7,3]), 6);


if __name__ == '__main__':
    unittest.main();