class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        left = [-1]*n
        candles = []
        temp, count = -1,0
        for i in range(len(s)):
            if s[i]=='|':
                count+=1
                temp = i
            candles.append(count)
            left[i] = temp
        
        right = [-1]*n
        temp = -1
        for i in range(n-1,-1,-1):
            if s[i]=='|':
                temp = i
            right[i] = temp
        print(right)
        
        res = [0]*len(queries)
        for i in range(len(queries)):
            l,r = queries[i][0], queries[i][1]
            nl, nr = right[l], left[r]
            if nl==-1 or nr==-1:
                res[i]=0
            else:
                dist = nr-nl
                if dist<0:
                    res[i] = 0
                else:
                    res[i] = (nr-nl+1) - (candles[nr]-candles[nl]+1)
        return res
                