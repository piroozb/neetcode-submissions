class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        longest = 0
        curr_sequences = {}
        for num in nums:
            if num - 1 not in hash_set:
                curr_sequences[num] = 1
                curr = num + 1
                while curr in hash_set:
                    curr_sequences[num] += 1
                    curr += 1
        
        return max(curr_sequences.values()) if nums else 0