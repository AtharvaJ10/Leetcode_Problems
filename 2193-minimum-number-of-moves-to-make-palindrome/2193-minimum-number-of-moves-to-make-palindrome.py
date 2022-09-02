class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        res = 0
        l,r = 0, len(s)-1
        while l<r:
            char = s[l]
            k = r
            while k>l and s[l]!=s[k]:
                k-=1
            if k==l:
                s[l],s[l+1] = s[l+1],s[l]
                res+=1
            else:
                while k<r:
                    s[k],s[k+1] = s[k+1], s[k]
                    k+=1
                    res+=1
                l,r = l+1,r-1
        return res