class Node:
    def __init__(self, url):
        self.url = url
        self.next = self.prev = None
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.dll = Node(homepage)
        self.current = self.dll

    def visit(self, url: str) -> None:
        self.new = Node(url)
        self.current.next = self.new
        self.new.prev = self.current
        self.current = self.current.next

    def back(self, steps: int) -> str:
        count = 0
        while count!=steps and self.current.prev is not None:
            self.current = self.current.prev
            count+=1
        return self.current.url

    def forward(self, steps: int) -> str:
        count = 0
        while count!=steps and self.current.next is not None:
            self.current = self.current.next
            count+=1
        return self.current.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)