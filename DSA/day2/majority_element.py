class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()

        for i in nums:
            d[i] = d.get(i,0) + 1
        
        for key,value in d.items():
            if value> len(nums)//2:
                return key
        
        return -1
