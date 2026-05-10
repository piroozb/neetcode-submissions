class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        s = s.replace(" ", "")
        r = len(s) - 1
        while l < r:
            while not s[r].isalnum() and r > 0:
                r -= 1
            while not s[l].isalnum() and l < r:
                l += 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True