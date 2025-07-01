class Solution():
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #solution using hash table (using linear time and linear space)
        hash = [0] * (len(nums) + 1)

        for i in nums:
            hash[i] += 1
        
        for i in range(1,len(hash)):
            if hash[i] > 1:
                return i
        return -1
    
        #solution using sorting( using constant space )
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
        return -1
    
sol = Solution()
print(sol.findDuplicate([1, 3, 4, 2, 2]))