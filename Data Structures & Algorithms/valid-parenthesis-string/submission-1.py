class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star_stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
            else:
                star_stack.append(i)
        
        if not stack:
            return True
        else:
            while stack and star_stack:
                curr_par = stack.pop()
                curr_star = star_stack.pop()

                if curr_par > curr_star:
                    return False
            
            return not stack