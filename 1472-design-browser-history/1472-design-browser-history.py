class Node:
    def __init__(self, url):
        self.url = url
        self.next = self.prev = None
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.cur = self.head

    def visit(self, url: str) -> None:
        self.cur.next = Node(url)
        self.cur.next.prev = self.cur
        self.cur = self.cur.next
                            
    def back(self, steps: int) -> str:
        while self.cur.prev and steps!=0:
            self.cur = self.cur.prev
            steps-=1
        return self.cur.url

    def forward(self, steps: int) -> str:
        while self.cur.next and steps!=0:
            self.cur = self.cur.next
            steps-=1
        return self.cur.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)