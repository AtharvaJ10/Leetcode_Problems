class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):
            return False
        
        res = 0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                res+=1
        
        if (Counter(s1)==Counter(s2)) and (res==0 or res==2):
            return True
        else:
            return False