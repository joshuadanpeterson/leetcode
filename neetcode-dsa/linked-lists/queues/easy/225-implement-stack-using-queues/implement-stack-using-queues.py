class MyStack:

    def __init__(self):
        self.queue = deque()
        

    def push(self, x: int) -> None:
        q = self.queue
        q.append(x)
        # Rotate the queue to place the new element at the front
        for _ in range(len(q) - 1):
            q.append(q.popleft())
        

    def pop(self) -> int:
        return self.queue.popleft()
        

    def top(self) -> int:
        return self.queue[0]
        

    def empty(self) -> bool:
        return not self.queue
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()