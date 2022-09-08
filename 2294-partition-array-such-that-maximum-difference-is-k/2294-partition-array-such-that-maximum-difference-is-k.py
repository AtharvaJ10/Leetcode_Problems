class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        mn = mx = nums[0]
        res = 1
        for i in nums:
            mn = min(mn, i)
            mx = max(mx, i)
            if mx-mn>k:
                res+=1
                mx = mn = i
        return res