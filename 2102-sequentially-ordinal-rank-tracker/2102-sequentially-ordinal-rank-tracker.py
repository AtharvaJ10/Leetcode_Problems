class h1:
    def __init__(self, name, score):
        self.name= name
        self.score = score
    
    def __lt__(self, other):
        return self.score>other.score or (self.score==other.score and self.name<other.name)
    
    def toh2(self):
        return h2(self.name, self.score)

class h2:
    def __init__(self, name, score):
        self.name= name
        self.score = score
    
    def __lt__(self, other):
        return self.score<other.score or (self.score==other.score and self.name>other.name)
    
    def toh1(self):
        return h1(self.name, self.score)
    
class SORTracker:

    def __init__(self):
        self.max = []
        self.min = []

    def add(self, name: str, score: int) -> None:
        n1 = h1(name,score)
        n2 = h2(name,score)
        if not self.min or self.min[0]>n2:
            heapq.heappush(self.max, n1)
        else:
            heapq.heappush(self.min, n2)
            node = heapq.heappop(self.min)
            heapq.heappush(self.max, node.toh1())

    def get(self) -> str:
        node = heapq.heappop(self.max)
        heapq.heappush(self.min, node.toh2())
        return node.name


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()