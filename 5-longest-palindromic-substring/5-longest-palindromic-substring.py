class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            odd = self.check(i,i,s)
            even = self.check(i,i+1,s)
            res = max(res, odd, even, key=len)
        return res
    
    def check(self, l, r, s):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]