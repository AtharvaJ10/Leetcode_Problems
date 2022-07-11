import math, heapq
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = [-1]
        i = 2
        while len(factors)<k and i<=(n//2):
            if n%i==0:
                heapq.heappush(factors,-i)
            i+=1
        if len(factors)<k-1:
            return -1
        elif len(factors)<k:
            return n
        return -factors[0]