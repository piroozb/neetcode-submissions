class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        
        half = total // 2
        n = len(nums)
        memo = [[-1] * (half + 1) for _ in range(n + 1)]

        def canPart(i, currSum):
            if i >= len(nums):
                return currSum == 0
            if memo[i][currSum] != -1:
                return memo[i][currSum]
            if currSum < 0:
                return False
            memo[i][currSum] = (canPart(i + 1, currSum) or canPart(i + 1, currSum - nums[i]))
            return memo[i][currSum]
        
        return canPart(0, half)
        