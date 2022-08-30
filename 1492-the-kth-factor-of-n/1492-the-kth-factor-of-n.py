class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, int(math.sqrt(n))+1):
            if n%i==0:
                factors.append(i)
        for i in range(len(factors)-1,-1,-1):
            factors.append(n//factors[i])
            if factors[-1]==factors[-2]:
                factors.pop()
        return factors[k-1] if k<=len(factors) else -1
    
        """isqrt = math.isqrt(n)
        for i in range(1, isqrt + 1):
            if n % i == 0:
			    k -= 1
                if k == 0: return i
        for i in reversed(range(1, isqrt + 1)):
            if i * i == n: continue
            if n % i == 0:
			    k -= 1
                if k == 0: return n // i
        return -1"""