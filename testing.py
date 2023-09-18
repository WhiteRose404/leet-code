import unittest
import random as rand
from solution import Solution

class Test(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName);
        self.largeArray = self.generateArray(8192, random = True);
        self.veryLargeArray = self.generateArray(12000, sequential = True);
    

    def generateArray(self, length, random = False, sequential = False):
        if(sequential): return [i for i in range(length, 0, -1)];
        elif(random): return [rand.randint(0, 10000) for i in range(length)];
        else: return [];

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
    
    def test7(self):
        correctAnswer = Solution().attempt(self.largeArray);
        self.assertEqual(Solution().candy(self.largeArray), correctAnswer);

    def test8(self):
        correctAnswer = Solution().attempt(self.veryLargeArray);
        self.assertEqual(Solution().candy(self.veryLargeArray), correctAnswer);

    def test9(self):
        arr = self.generateArray(20, random = True);
        self.assertEqual(Solution().candy(arr), Solution().attempt(arr));
if __name__ == '__main__':
    unittest.main();