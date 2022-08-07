class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d = defaultdict(int)
        for i in s:
            d[i]+=1
        
        count = 0
        for i in t:
            if d[i]:
                d[i]-=1
            else:
                count+=1
        return count