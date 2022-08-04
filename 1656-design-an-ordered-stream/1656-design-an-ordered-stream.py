class OrderedStream:

    def __init__(self, n: int):
        self.result = [None]*(n+1)
        self.start = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.result[idKey] = value
        res = []
        if idKey==self.start:
            while self.start<len(self.result) and self.result[self.start] is not None:
                res.append(self.result[self.start])
                self.start+=1
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)