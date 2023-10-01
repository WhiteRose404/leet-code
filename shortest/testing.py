import unittest
from solution import Solution

def modify(fn):
    def wrapper(*args, **kwargs):
        print("New test case")
        return fn(*args, **kwargs);
    return wrapper

class Testing(unittest.TestCase):
    @modify
    def test1(self):
        self.assertEqual(Solution().shortest([[1,2],[0,2],[0,1]]), 4);
    @modify
    def test2(self):
        self.assertEqual(Solution().shortest([[0,1],[0,2],[1,3],[2,1]]), 4);
    @modify
    def test3(self):
        self.assertEqual(Solution().shortest([[0,1],[0,2],[1,3]]), 4);

if __name__ == '__main__':
    unittest.main()
    