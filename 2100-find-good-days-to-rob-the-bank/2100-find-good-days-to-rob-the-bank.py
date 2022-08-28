class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        left = [0]
        l,n = 0, len(security)
        for i in range(1, n):
            if security[i]<=security[i-1]:
                l+=1
            else:
                l = 0
            left.append(l)
            
        right = [0]*n
        r = 0
        for i in range(n-2,-1,-1):
            if security[i]<=security[i+1]:
                r+=1
            else:
                r = 0
            right[i] = r
        
        return [i for i in range(n) if left[i]>=time and right[i]>=time]