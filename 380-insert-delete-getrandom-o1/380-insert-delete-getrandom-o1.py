import random
class RandomizedSet:

    def __init__(self):
        self.values = []
        self.indices = defaultdict(int)

    def insert(self, val: int) -> bool:
        if val not in self.indices:
            self.values.append(val)
            self.indices[val] = len(self.values)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.indices:
            out_index = self.indices[val]
            insert_val = self.values[-1]
            self.values[out_index] = insert_val
            self.indices[insert_val] = out_index
            del self.indices[val]
            self.values.pop()
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()