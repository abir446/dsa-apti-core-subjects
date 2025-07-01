class Solution():
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = dict()
        for i in range(len(nums)):
            more = target - nums[i]
            if more in hash:
                return [hash[more],i]
            hash[nums[i]] = i
        return [-1,-1]

sol = Solution()
sol.twoSum([2, 7, 11, 15], 9)