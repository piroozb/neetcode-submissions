class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_keys = {}
        for char in s:
            s_keys[char] = s_keys.get(char, 0) + 1
        t_keys = {}
        for char in t:
            t_keys[char] = t_keys.get(char, 0) + 1
        
        return t_keys == s_keys