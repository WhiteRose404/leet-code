
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
        #############################
        ##### needs to be fixed #####
        ##  req: unmodified array  ##
        #############################

        res = -1;
        for i in range(len(nums)):
            target = abs(nums[i]);
            if nums[target] < 0:
                res = target;
                break;
            nums[target] = -nums[target];
        for j in range(len(nums)):
            nums[j] = abs(nums[j]);
        
        return res;

