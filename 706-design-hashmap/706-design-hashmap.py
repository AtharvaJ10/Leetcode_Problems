from collections import defaultdict
class MyHashMap:

    def __init__(self):
        self.d = defaultdict(lambda: -2)
        

    def put(self, key: int, value: int) -> None:
        self.d[key] = value
        

    def get(self, key: int) -> int:
        if self.d[key]==-2:
            return -1
        return self.d[key]
        

    def remove(self, key: int) -> None:
        if self.d[key]!=-2:
            del self.d[key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)