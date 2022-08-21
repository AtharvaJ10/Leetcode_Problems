class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        res = 0
        while s:
            i = s.index(s[-1])
            if i==len(s)-1:    #odd case
                res+=i//2
            else:
                res+=i
                s.pop(i)
            s.pop()
        return res