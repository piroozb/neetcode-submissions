class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
        
        count2 = [0] * 26
        l = 0
        for r in range(len(s2)):
            count2[ord(s2[r]) - ord('a')] += 1
            if r - l + 1 == len(s1):
                if count2 == count1:
                    return True
            while r - l + 1 > len(s1):
                count2[ord(s2[l]) - ord('a')] -= 1
                l += 1
                if count2 == count1:
                    return True
        
        return False