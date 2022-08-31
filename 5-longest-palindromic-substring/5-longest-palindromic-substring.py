class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            odd = self.helper(i,i,s)
            even = self.helper(i,i+1,s)
            res = max(odd, even, res, key=len)
        return res
    
    def helper(self, l, r, s):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]