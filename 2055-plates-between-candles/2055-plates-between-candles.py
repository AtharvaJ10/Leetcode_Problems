class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        left = [-1]*n
        candles =[]
        count, c = 0,-1
        for i in range(n):
            if s[i]=='|':
                c = i
                count+=1
            left[i] = c
            candles.append(count)
        
        right = [-1]*n
        c = -1
        for i in range(n-1,-1,-1):
            if s[i]=='|':
                c = i
            right[i] = c
        
        res=[]
        for i,j in queries:
            start = right[i]
            end = left[j]
            if start==-1 or end==-1:
                res.append(0)
            else:
                dist = end - start
                if dist>0:
                    temp = end-start+1 - (candles[end] - candles[start]+1)
                    res.append(temp)
                else:
                    res.append(0)
        return res