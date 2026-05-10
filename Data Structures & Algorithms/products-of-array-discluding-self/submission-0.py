class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for i in range(len(nums) - 1):
            prefix.append(prefix[-1] * nums[i])
        
        suffix = [1]
        for i in range(len(nums) - 1, 0, -1):
            suffix.append(suffix[-1] * nums[i])
        suffix.reverse()

        return [prefix[i] * suffix[i] for i in range(len(prefix))]