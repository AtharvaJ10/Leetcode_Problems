import random
class RandomizedCollection:

    def __init__(self):
        self.indexes = defaultdict(set)
        self.values = []

    def insert(self, val: int) -> bool:
        self.values.append(val)
        self.indexes[val].add(len(self.values)-1)
        return len(self.indexes[val])==1

    def remove(self, val: int) -> bool:
        if self.indexes[val]:
            out_index = self.indexes[val].pop()
            insert_val = self.values[-1]
            self.values[out_index] = insert_val
            self.indexes[insert_val].add(out_index)
            self.indexes[insert_val].discard(len(self.values)-1)
            self.values.pop()
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()