class Bitset(object):

    def __init__(self, size):
        self.a = 0     #bitset
        self.size = size
        self.cnt = 0   # count of ones

    def fix(self, idx):
        if self.a & (1 << idx) == 0:    # 'and' and left shift
            self.a |= 1 << idx          # or
            self.cnt += 1

    def unfix(self, idx):
        if self.a & (1 << idx):     
            self.a ^= 1 << idx          # xor
            self.cnt -= 1

    def flip(self):
        self.a ^= (1 << self.size) - 1  # first minus then xor
        self.cnt = self.size - self.cnt

    def all(self):
        return self.cnt == self.size

    def one(self):
        return self.a > 0

    def count(self):
        return self.cnt

    def toString(self):
        a = bin(self.a)[2:]     #convert to binary string
        return a[::-1] + '0' * (self.size - len(a))

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()