class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()

        for i in range(len(nums)):
            more = target - nums[i]

            if more in d:
                return [d[more],i]
            d[nums[i]] = i

        return [-1,-1]
        
