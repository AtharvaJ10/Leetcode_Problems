class Node:
    def __init__(self, url):
        self.url = url
        self.next = self.prev = None
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = Node(homepage)

    def visit(self, url: str) -> None:
        self.history.next = Node(url)
        self.history.next.prev = self.history
        self.history = self.history.next

    def back(self, steps: int) -> str:
        while steps and self.history.prev:
            self.history = self.history.prev
            steps-=1
        return self.history.url

    def forward(self, steps: int) -> str:
        while steps and self.history.next:
            self.history = self.history.next
            steps-=1
        return self.history.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)