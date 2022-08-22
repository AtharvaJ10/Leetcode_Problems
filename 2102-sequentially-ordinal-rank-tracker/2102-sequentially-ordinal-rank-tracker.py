class h1Node:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __lt__(self, other):
        # higher score first
        # if same score, lexico smaller first
        return self.score > other.score or (self.score == other.score and self.name < other.name)

    def to_h2Node(self):
        return h2Node(self.name, self.score)

class h2Node:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __lt__(self, other):
        # lower score first
        # if same score, lexico greater first
        return self.score < other.score or (self.score == other.score and self.name > other.name)

    def to_h1Node(self):
        return h1Node(self.name, self.score)

class SORTracker:

    def __init__(self):
        from heapq import heappush, heappop
        self.heap1 = []
        self.heap2 = []

    def add(self, name: str, score: int) -> None:
        h1node = h1Node(name, score)
        h2node = h2Node(name, score)
        if not self.heap2 or self.heap2[0] > h2node:
            heappush(self.heap1, h1node)
        else:
            heappush(self.heap2, h2node)
            node = heappop(self.heap2)
            heappush(self.heap1, node.to_h1Node())

    def get(self) -> str:
        node = heappop(self.heap1)
        heappush(self.heap2, node.to_h2Node())
        return node.name