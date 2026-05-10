class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def generate(curr="", nums_open=0, nums_closed=0):
            if nums_closed == n:
                res.append(curr)
            if nums_open + nums_closed == n:
                curr += ")" * nums_open
                res.append(curr)
            else:
                if nums_open < n:
                    generate(curr + "(", nums_open + 1, nums_closed)
                if nums_closed < n and nums_open >= 1:
                    generate(curr + ")", nums_open - 1, nums_closed + 1)
        
        generate()
        return res
            