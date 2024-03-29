class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        res = 0
        while s:
            index = s.index(s[-1])
            if index == len(s)-1:
                res+=index//2
            else:
                res+=index
                s.pop(index)
            s.pop()
        return res