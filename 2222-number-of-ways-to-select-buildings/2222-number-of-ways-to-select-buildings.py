class Solution:
    def numberOfWays(self, s: str) -> int:
        a,b,res = 0,0,0
        for i in range(len(s)):
            if s[i]=="1":
                a+=1
            else:
                b+=1
        
        c,d = 0,0
        for i in range(len(s)):
            if s[i]=="1":
                res+= (b*d)
                a-=1
                c+=1
            else:
                res+=(a*c)
                b-=1
                d+=1
        
        return res