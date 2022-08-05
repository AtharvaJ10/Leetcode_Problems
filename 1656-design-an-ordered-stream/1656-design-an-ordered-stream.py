class OrderedStream:

    def __init__(self, n: int):
        self.res = [None] * (n+1)
        self.start = 1
        
    def insert(self, idKey: int, value: str) -> List[str]:
        self.res[idKey] = value
        res = []
        if idKey==self.start:
            while self.start<len(self.res) and self.res[self.start]:
                res.append(self.res[self.start])
                self.start+=1
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)