class BrowserHistory:

    def __init__(self, homepage: str):
        self.prev = []
        self.fwd = []
        self.cur = homepage

    def visit(self, url: str) -> None:
        self.prev.append(self.cur)
        self.fwd = []
        self.cur = url

    def back(self, steps: int) -> str:
        num = min(steps, len(self.prev))
        while num:
            self.fwd.append(self.cur)
            self.cur = self.prev.pop()
            num-=1
        return self.cur

    def forward(self, steps: int) -> str:
        num = min(steps, len(self.fwd))
        while num:
            self.prev.append(self.cur)
            self.cur = self.fwd.pop()
            num-=1
        return self.cur


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)