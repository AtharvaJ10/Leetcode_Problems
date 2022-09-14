class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        for num in sorted(arr):
            if num in rank:
                continue
            rank[num] = len(rank)+1
        
        res = []
        for i in arr:
            res.append(rank[i])
        return res