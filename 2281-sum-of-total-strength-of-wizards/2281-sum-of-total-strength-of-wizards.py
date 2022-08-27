class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        n = len(strength)
        right = [n]*n
        stack = []
        for i in range(n):
            while stack and strength[stack[-1]]>strength[i]:
                right[stack.pop()] = i
            stack.append(i)
        
        left = [-1]*n
        stack = []
        for i in range(n-1,-1,-1):
            while stack and strength[stack[-1]]>=strength[i]:
                left[stack.pop()] = i
            stack.append(i)
        
        pre = [0]
        for i in strength:
            pre.append(pre[-1]+i)
        for i in range(1, len(pre)):
            pre[i]+=pre[i-1]
        
        res = 0
        for i in range(n):
            l,r = left[i], right[i]
            lrange, rrange = i-l, r-i
            lsum,rsum = pre[i]-pre[max(l,0)], pre[r]-pre[i]
            res+=strength[i]*(rsum*lrange - lsum*rrange)
        res%=(10**9+7)
        return res