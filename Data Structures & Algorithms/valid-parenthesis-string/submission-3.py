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

        while stack and star_stack:
            if stack.pop() > star_stack.pop():
                return False
        
        return not stack