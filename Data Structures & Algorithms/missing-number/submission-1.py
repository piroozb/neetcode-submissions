class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(1, n+1):
            res ^= i
        
        for i in range(n):
            res ^= nums[i]
        
        return res