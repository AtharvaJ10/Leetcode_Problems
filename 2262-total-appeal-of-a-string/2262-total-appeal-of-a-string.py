class Solution:
    def appealSum(self, s: str) -> int:
        last = defaultdict(lambda:-1)
        res = 0
        for i,c in enumerate(s):
            j = last[c]
            res+=(len(s)-i)*(i-j)
            last[c] = i
        return res
        