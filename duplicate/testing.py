import unittest
import random

from solution import Solution

class Testing(unittest.TestCase):
    def generatArray(self, n):
        sequence = [i for i in range(1, n)];
        repeat = random.randint(1, n - 1);
        res = [];
        for i in range(0, n):
            randomIndex = 0 if len(sequence) == 1 else random.randint(0, len(sequence) - 1);
            if(sequence[randomIndex] == repeat):
                res.append(sequence[randomIndex]);
            else:
                res.append(sequence.pop(randomIndex));
        return res;

    # simple tests
    def test1(self):
        self.assertEqual(Solution().duplicate([1, 1]), 1);
    def test2(self):
        self.assertEqual(Solution().duplicate([1, 2, 3, 4, 1]), 1);
    def test3(self):
        self.assertEqual(Solution().duplicate([1, 2, 3, 4, 5, 5]), 5);

    # random cases
    def test14(self):
        test_arr = self.generatArray(7);
        self.assertEqual(Solution().duplicate(test_arr), Solution().sol(test_arr));
    def test12(self):
        test_arr = self.generatArray(5);
        self.assertEqual(Solution().duplicate(test_arr), Solution().sol(test_arr));
    def test20(self):
        test_arr = self.generatArray(10);
        self.assertEqual(Solution().duplicate(test_arr), Solution().sol(test_arr));
    def test4(self):
        test_arr = self.generatArray(80);
        self.assertEqual(Solution().duplicate(test_arr), Solution().sol(test_arr));
    def test5(self):
        test_arr = self.generatArray(5000);
        self.assertEqual(Solution().duplicate(test_arr), Solution().sol(test_arr));
    def test6(self):
        test_arr = self.generatArray(2000);
        self.assertEqual(Solution().duplicate(test_arr), Solution().sol(test_arr));
    def test7(self):
        test_arr = self.generatArray(300);
        self.assertEqual(Solution().duplicate(test_arr), Solution().sol(test_arr));
    def test8(self):
        test_arr = self.generatArray(1000);
        self.assertEqual(Solution().duplicate(test_arr), Solution().sol(test_arr));


if __name__ == '__main__':
    unittest.main()