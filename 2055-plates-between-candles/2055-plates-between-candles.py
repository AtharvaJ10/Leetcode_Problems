class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n,l,count = len(s),-1,0
        left = [-1]*n
        candles = []
        for i in range(n):
            if s[i]=='|':
                l = i
                count+=1
            candles.append(count)
            left[i] = l
        
        right = [-1]*n
        r = -1
        for i in range(n-1,-1,-1):
            if s[i]=='|':
                r = i
            right[i] = r
        
        res = []
        for i,j in queries:
            st, end = right[i], left[j]
            if st==-1 or end==-1:
                res.append(0)
            else:
                dist = end-st
                if dist<0:
                    res.append(0)
                else:
                    temp = dist+1-(candles[end]-candles[st]+1)
                    res.append(temp)
        return res
        
        