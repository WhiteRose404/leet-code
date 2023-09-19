
class Solution:

    # invalid solution: it uses O(n) space
    def sol(self, nums) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        # print(nums)
        seen = set()
        for num in nums:
            if num in seen:
                return num;
            seen.add(num)
        return -1;

    def duplicate(self, nums) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        # s = sum(nums);
        # m = max(nums);
        # n = len(nums);
        # print("arr: ", nums, "sum: ", s, "max: ", m, "len: ", n)
        # for k in nums:
            # sum_k = k*(k-1)//2;
            # sum_k_m = max(k*(m-k-1), 0);
            # sum_k_n = k*(n-m+1);
            # sum_k_k = ((m-k)*(m-k-1))//2;
            # print("k: ", k, "itr: ", sum_k, sum_k_m, sum_k_n, sum_k_k)
            # itr = sum_k + sum_k_m + sum_k_n + sum_k_k;
            # if(s == itr): return k;
            # print(k, itr, s)
        return -1;

