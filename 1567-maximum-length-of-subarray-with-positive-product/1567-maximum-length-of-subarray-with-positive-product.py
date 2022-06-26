class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos, neg, res = 0, 0, 0
        for i in nums:
            if i>0:
                pos, neg = pos+1, neg+1 if neg else 0
            elif i<0:
                pos, neg = neg+1 if neg else 0, pos+1
            else:
                pos, neg = 0, 0
            res = max(res, pos)
        return res