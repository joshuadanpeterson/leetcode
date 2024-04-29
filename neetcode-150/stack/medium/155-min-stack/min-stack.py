class MinStack:
    def __init__(self):
        # Initialize two stacks
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # Push the value onto the main stack
        self.stack.append(val)
        # Push the value onto the min stack if it is the new minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Pop the value from the main stack
        val = self.stack.pop()
        # If it is the minimum, pop it from the min stack as well
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        # Return the top value of the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the top value of the min stack
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()