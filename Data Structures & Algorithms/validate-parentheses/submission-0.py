class Solution:
    def isValid(self, s: str) -> bool:
        closed = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in closed and stack and stack[-1] == closed[char]:
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0
