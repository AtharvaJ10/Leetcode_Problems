class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum1,count = 0,0
        d = dict()
        d[0] = 1
        
        for i in range(len(nums)):
            sum1+=nums[i]
            count+=d.get(sum1-k,0)
            d[sum1] = d.get(sum1,0)+1
        return count
        