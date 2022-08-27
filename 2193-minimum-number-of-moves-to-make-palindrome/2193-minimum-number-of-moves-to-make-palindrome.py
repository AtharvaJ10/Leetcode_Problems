class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        l = list(s)
        res = 0
        while l:
            index = l.index(l[-1])
            if index == len(l)-1:
                res+=index//2
            else:
                res+=index
                l.pop(index)
            l.pop()
        return res