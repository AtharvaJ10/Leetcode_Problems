class Solution:
    def appealSum(self, s: str) -> int:
        last = {c:-1 for c in ascii_lowercase}
        res = 0
        for i,c in enumerate(s):
            j = last[c]
            res+=(len(s)-i)*(i-j)
            last[c] = i
        return res