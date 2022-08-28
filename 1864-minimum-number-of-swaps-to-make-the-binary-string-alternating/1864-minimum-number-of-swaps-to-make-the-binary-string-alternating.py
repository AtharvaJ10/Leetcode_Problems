class Solution:
    def minSwaps(self, s: str) -> int:
        def swap(x):
            res = 0
            for i in s:
                if i!=x:
                    res+=1
                if x=="1":
                    x = "0"
                else:
                    x = "1"
            return res//2
        
        ones = s.count("1")
        zeros = len(s) - ones
        
        if abs(ones-zeros)>1:
            return -1
        
        if ones>zeros:
            return swap("1")
        elif zeros>ones:
            return swap("0")
        else:
            return min(swap("1"), swap("0"))