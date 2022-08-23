class Solution:
    def totalStrength(self, A: List[int]) -> int:
        n = len(A)
        right = [n]*n
        stack = []
        for i in range(len(A)):
            while stack and A[stack[-1]]>A[i]:
                right[stack.pop()] = i
            stack.append(i)
            
        left = [-1]*n
        stack = []
        for i in range(len(A)-1,-1,-1):
            while stack and A[stack[-1]]>=A[i]:
                left[stack.pop()] = i
            stack.append(i)
        
        prefix = [0]
        for i in A:
            prefix.append(prefix[-1]+i)
        
        for i in range(1, len(prefix)):
            prefix[i]+=prefix[i-1]
        
        res = 0
        for i in range(len(A)):
            l,r = left[i], right[i]
            l_range, r_range = i-l, r-i
            lsum = prefix[i] - prefix[max(l,0)]
            rsum = prefix[r] - prefix[i]
            res+=A[i]*(rsum*l_range - lsum*r_range)
        return res % (10**9 + 7)
                      