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
        
        prefix_sum = [0]
        for i in range(n):
            prefix_sum.append(prefix_sum[-1]+strength[i])
        
        for i in range(1,n+1):
            prefix_sum[i] = prefix_sum[i]+prefix_sum[i-1]

        res = 0
        for i in range(n):
            l,r = left[i], right[i]
            l_sum = prefix_sum[i] - prefix_sum[max(l,0)]
            r_sum = prefix_sum[r] - prefix_sum[i]
            l_range = i-l
            r_range = r-i
            res+= strength[i]* (r_sum*l_range - l_sum * r_range)
        return res %(10**9 + 7)
        
        
        