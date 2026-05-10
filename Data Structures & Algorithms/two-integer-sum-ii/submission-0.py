class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        comp = {}
        for i in range(len(numbers)):
            curr = target - numbers[i]
            if curr in comp:
                return [comp[curr] + 1, i + 1]
            comp[numbers[i]] = i