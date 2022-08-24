import math
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = [1]
        for i in range(2, int(math.sqrt(n))+1):
            if n%i==0:
                factors.append(i)
        
        for i in range(len(factors)-1,-1,-1):
            factors.append(n//factors[i])
            if factors[-1]==factors[-2]:
                factors.pop()
        
        return factors[k-1] if k<=len(factors) else -1