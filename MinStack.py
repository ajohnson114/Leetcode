class MinStack:
"""
Simple basic python kind of. Read list concatenation and indexing if you're confused. For the final for loop you might want to set initial minimum to 
self.stack[0] and then see if any of the values are smaller than that when you iterate. 
"""
    def __init__(self):
        self.stack =  []

    def push(self, val: int) -> None:
        self.stack.append(val) #can also do self.stack += [val]
        
    def pop(self) -> None:
        self.stack.pop() # can also do self.stack = self.stack[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack) #can also do a for loop


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
