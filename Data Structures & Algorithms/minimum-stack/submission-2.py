class MinStack:

    def __init__(self):
        self.stack = []
        self.currMin = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val - self.currMin)
        if val < self.currMin:
            self.currMin = val

    def pop(self) -> None:
        curr = self.stack.pop()
        if curr < 0:
            self.currMin = self.currMin - curr

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.currMin
        else:
            return self.currMin

    def getMin(self) -> int:
        return self.currMin
        
