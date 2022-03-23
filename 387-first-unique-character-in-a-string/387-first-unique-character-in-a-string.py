class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = dict()
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]][0]+=1
            else:
                d[s[i]] = [1,i]
                
        min1 = len(s)
        for i in d:
            print(d)
            if d[i][0]==1 and d[i][1]<min1:
                min1=d[i][1]
        if min1==len(s):
            return -1
        return min1
                