import random
from collections import defaultdict
class RandomizedCollection:

    def __init__(self):
        self.value = []
        self.index = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.value.append(val)
        self.index[val].add(len(self.value)-1)
        return len(self.index[val])==1
            

    def remove(self, val: int) -> bool:
        if self.index[val]:
            out = self.index[val].pop()
            insert = self.value[-1]
            self.value[out] = insert
            self.index[insert].add(out)
            self.index[insert].discard(len(self.value)-1)
            self.value.pop()
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.value)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()