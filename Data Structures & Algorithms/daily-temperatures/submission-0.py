class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0] # stack of indices
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                result[prev_idx] = i - prev_idx
            stack.append(i)
        return result
        
