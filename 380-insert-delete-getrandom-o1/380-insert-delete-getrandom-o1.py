import random
class RandomizedSet:

    def __init__(self):
        self.values = []
        self.indexes = defaultdict(int)

    def insert(self, val: int) -> bool:
        if val not in self.indexes:
            self.values.append(val)
            self.indexes[val] = len(self.values)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.indexes:
            return False
        out_index = self.indexes[val]
        insert_value = self.values[-1]
        self.values[out_index] = insert_value
        self.indexes[insert_value] = out_index
        self.indexes.pop(val)
        self.values.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()