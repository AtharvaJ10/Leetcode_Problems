class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        curr,n = 0, len(nums)
        rem = sum(nums)
        res = float('inf')
        ind = 0
        for i in range(len(nums)):
            curr+=nums[i]
            rem-=nums[i]
            avg1 = curr//(i+1)
            avg2 = rem//(n-i-1) if i!=n-1 else rem
            if abs(avg1-avg2)<res:
                res = abs(avg1-avg2)
                ind = i
        return ind