class MinStack:

    def __init__(self):
        self.stack=[]
        self.small=float('inf')

    def push(self, val: int) -> None:
        self.small=min(self.small,val)
        self.stack.append((val,self.small))
    
    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.small=self.stack[-1][1]
        else:
            self.small=float('inf')

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
