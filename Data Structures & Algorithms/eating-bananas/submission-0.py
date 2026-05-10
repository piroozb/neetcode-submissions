import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper_bound = max(piles)
        lower_bound = 1
        k = upper_bound
        while lower_bound <= upper_bound:
            curr_k = (upper_bound + lower_bound) // 2
            curr_h = 0
            for pile in piles:
                curr_h += math.ceil(pile / curr_k)
            if curr_h <= h:
                k = curr_k
                upper_bound = curr_k - 1
            else:
                lower_bound = curr_k + 1
        
        return k