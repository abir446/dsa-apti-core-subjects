class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = []
        for i in nums:
            if i not in temp:
                temp.append(i)
        
        i = 0
        for item in temp:
            nums[i] = item
            i += 1
        return i
        
        
sol = Solution()
print(sol.removeDuplicates([1, 1, 2]))

