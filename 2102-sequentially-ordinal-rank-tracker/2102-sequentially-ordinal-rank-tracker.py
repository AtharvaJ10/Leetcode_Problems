import heapq

class h1Node:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __lt__(self, other):
        return self.score>other.score or (self.score==other.score and self.name<other.name)
    
    def to_h2(self):
        return h2Node(self.name, self.score)
    
class h2Node:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __lt__(self, other):
        return self.score<other.score or (self.score==other.score and self.name>other.name)
    
    def to_h1(self):
        return h1Node(self.name, self.score)
    
    
class SORTracker:

    def __init__(self):
        self.max = []
        self.min = []

    def add(self, name: str, score: int) -> None:
        n1 = h1Node(name, score)
        n2 = h2Node(name, score)
        if not self.min or self.min[0]>n2:
            heapq.heappush(self.max, n1)
        else:
            heapq.heappush(self.min, n2)
            node = heapq.heappop(self.min)
            heapq.heappush(self.max, node.to_h1())

    def get(self) -> str:
        node = heapq.heappop(self.max)
        heapq.heappush(self.min, node.to_h2())
        return node.name


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()