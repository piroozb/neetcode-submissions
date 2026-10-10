class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        output = [0, 1]
        offset = 2
        for i in range(2, n+1):
            if offset * 2 == i:
                offset = i
            output.append(1 + output[i - offset])
        
        return output