class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        res = 1
        nums.sort()
        mn = mx = nums[0]
        for i in range(1, len(nums)):
            mx = max(mx, nums[i])
            mn = min(mn, nums[i])
            if mx-mn>k:
                res+=1
                mx = mn = nums[i]
        return res
                