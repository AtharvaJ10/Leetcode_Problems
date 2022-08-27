class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n,ncr,res = len(nums)-1,1,0
        for i,r in enumerate(nums):
            res = (res + r*ncr)%10
            ncr = ncr*(n-i)//(i+1)
        return res