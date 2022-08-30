class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = suffix = 1
        res = [1]*len(nums)
        for i in range(len(nums)):
            res[i]*=prefix
            prefix*=nums[i]
            res[len(nums)-i-1]*=suffix
            suffix*=nums[-1-i]
        return res