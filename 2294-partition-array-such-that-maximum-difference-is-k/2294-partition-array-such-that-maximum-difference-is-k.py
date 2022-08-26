class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 1
        mn = mx = nums[0]
        for i in nums:
            mn = min(mn, i)
            mx = max(mx, i)
            if mx-mn>k:
                res+=1
                mn = mx = i
        return res