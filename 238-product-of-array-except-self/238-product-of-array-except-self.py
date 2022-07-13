class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix, res = 1, 1, [1 for i in nums]
        for i in range(len(nums)):
            res[i] *= prefix
            prefix*=nums[i]
            res[-1-i] *= suffix
            suffix*=nums[-1-i]
        return res