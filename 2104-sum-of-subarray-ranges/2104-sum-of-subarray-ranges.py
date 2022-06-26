class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(nums)+1):
            while stack and (i ==len(nums) or nums[stack[-1]]>nums[i]):
                j = stack.pop()
                k = stack[-1] if stack else -1
                res-= nums[j] * (i-j) * (j-k)
            stack.append(i)
        
        stack = []
        for i in range(len(nums)+1):
            while stack and (i ==len(nums) or nums[stack[-1]]<nums[i]):
                j = stack.pop()
                k = stack[-1] if stack else -1
                res+= nums[j] * (i-j) * (j-k)
            stack.append(i)
        return res
        