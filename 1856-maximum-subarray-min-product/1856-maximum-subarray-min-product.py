class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        right = [n]*n
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]]>nums[i]:
                right[stack.pop()] = i
            stack.append(i)
        
        left = [-1]*n
        stack = []
        for i in range(n-1,-1,-1):
            while stack and nums[stack[-1]]>=nums[i]:
                left[stack.pop()] = i
            stack.append(i)
        
        pre = [0]
        for i in nums:
            pre.append(pre[-1]+i)
            
        res = 0
        for i in range(len(nums)):
            l,r = left[i], right[i]
            res= max(res, nums[i]*(pre[r]-pre[l+1]))
            
        return res%(10**9 + 7)
        