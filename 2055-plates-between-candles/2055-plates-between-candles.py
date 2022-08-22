class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        nearest_right = []
        nearest_left = []
        candles = []
        
        left, count = -1, 0
        for i in range(len(s)):
            if s[i]=='|':
                left = i
                count+=1
            nearest_left.append(left)
            candles.append(count)
            
        right = -1
        for i in range(len(s)-1,-1,-1):
            if s[i]=='|':
                right = i
            nearest_right.append(right)
        nearest_right = nearest_right[::-1]
        
        ans = [0]*len(queries)
        for i in range(len(ans)):
            start = queries[i][0]
            end = queries[i][1]
            
            left , right = nearest_right[start], nearest_left[end]
            if left ==-1 or right == -1:
                ans[i] = 0
            else:
                dist = right - left
                if dist > 0:
                    ans[i] = right - left + 1 - (candles[right] - candles[left] +1)
                    # The count would be difference btn right and left nearest candle - number of candles in between.
                else:
                    ans[i] = 0
        return ans