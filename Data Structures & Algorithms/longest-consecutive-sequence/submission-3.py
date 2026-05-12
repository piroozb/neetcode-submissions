class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        longest = 0
        for num in nums:
            curr = 1
            while num + 1 in hash_set:
                curr += 1
                num += 1
            longest = max(longest, curr)
        
        return longest