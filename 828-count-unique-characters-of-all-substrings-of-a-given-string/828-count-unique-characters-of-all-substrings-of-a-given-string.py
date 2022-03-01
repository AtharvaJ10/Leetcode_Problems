class Solution:
    def uniqueLetterString(self, s: str) -> int:
        d = {c : [-1,-1] for c in string.ascii_uppercase}
        res = 0
        
        for i,c in enumerate(s):
            k,j = d[c]
            res+= (i-j) * (j-k)
            d[c] = [j,i]
        
        for i in d:
            k , j = d[i]
            res+= (len(s)-j) * (j-k)
        return res