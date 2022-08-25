class Solution:
    def minSwaps(self, s: str) -> int:
        ones = s.count("1")
        zeros = len(s)-ones
        if abs(ones-zeros)>1:
            return -1
        
        def compute(x):
            res = 0
            for c in s:
                if c!=x:
                    res+=1
                x = "1" if x=="0" else "0"
            return res//2
        
        if ones>zeros:
            return compute("1")
        elif zeros>ones:
            return compute("0")
        else:
            return min(compute("0"), compute("1"))