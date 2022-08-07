class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """d = defaultdict(int)
        for i in s:
            d[i]+=1
        
        count = 0
        for i in t:
            if d[i]:
                d[i]-=1
            else:
                count+=1
        return count"""
        
        array = [0]*26
        for i in range(len(s)):
            array[ord(s[i]) - ord('a')]+=1
            array[ord(t[i]) - ord('a')]-=1
        
        res = 0
        for i in array:
            if i>0:
                res+=i
        return res