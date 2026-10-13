class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set([n])
        while n != 1:
            curr = str(n)
            total = 0
            for char in curr:
                total += int(char) ** 2
            n = total
            if total in seen:
                return False
            seen.add(total)
        return True