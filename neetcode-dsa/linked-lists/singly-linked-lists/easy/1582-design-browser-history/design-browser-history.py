class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]  # This list stores all the pages visited.
        self.current = 0           # This index keeps track of the current page.

    def visit(self, url: str) -> None:
        # When visiting a new URL, discard all forward history.
        self.history = self.history[:self.current+1]
        self.history.append(url)
        self.current += 1

    def back(self, steps: int) -> str:
        # Move back by 'steps', but not beyond the start of the history.
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        # Move forward by 'steps', but not beyond the end of the history.
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)