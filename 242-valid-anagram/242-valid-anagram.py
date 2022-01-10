from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(lambda: "No")
        for i in s:
            if d[i] == "No":
                d[i] = 1
            else:
                d[i]+=1
        
        for i in t:
            if d[i] == "No" or d[i]== 0:
                return False
            else:
                d[i]-=1
        
        for i in d.keys():
            if d[i]!=0:
                return False
        return True
            