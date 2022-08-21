from collections import defaultdict
class Solution:
    def appealSum(self, s: str) -> int:
        d = defaultdict(lambda: -1)
        res = 0
        for i,c in enumerate(s):
            k = d[c]
            res+=(len(s)-i)*(i-k)
            d[c] = i
        return res