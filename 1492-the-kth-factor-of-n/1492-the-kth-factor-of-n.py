import math
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, int(math.sqrt(n))+1):
            if n%i ==0:
                factors.append(i)
        for i in range(len(factors)-1,-1,-1):
            factors.append(n//factors[i])
            if factors[-1]==factors[-2]:
                factors.pop()
        print(factors)
        if len(factors)<k:
            return -1
        return factors[k-1]