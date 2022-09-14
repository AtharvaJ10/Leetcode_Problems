class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cur = self.fwd = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.cur+1]
        self.history.append(url)
        self.cur+=1
        self.fwd = 0

    def back(self, steps: int) -> str:
        if self.cur>=steps:
            self.cur-=steps
            self.fwd+=steps
        else:
            self.fwd = len(self.history)-1
            self.cur = 0
        return self.history[self.cur]

    def forward(self, steps: int) -> str:
        if self.fwd>=steps:
            self.cur+=steps
            self.fwd-=steps
        else:
            self.fwd = 0
            self.cur = len(self.history)-1
        return self.history[self.cur]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)