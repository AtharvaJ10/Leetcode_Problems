class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res = 0
        prev = float('inf')
        c = 0
        for cur in prices:
            if prev-cur==1:
                c+=1
            else:
                c=1
            res+=c
            prev = cur
        return res
                