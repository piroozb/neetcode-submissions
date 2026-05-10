class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letters = {"2": "abc", "3": "def", "4": "ghi",  "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        combos = [char for char in letters[digits[0]]]
        for i in range(1, len(digits)):
            combos2 = []
            while combos:
                curr = combos.pop()
                for char in letters[digits[i]]:
                    curr2 = curr + char
                    combos2.append(curr2)
            combos = combos2
        
        return combos