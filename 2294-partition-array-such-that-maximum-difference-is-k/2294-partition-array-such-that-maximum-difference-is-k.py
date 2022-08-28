class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        mx = mn = nums[0]
        i = 0
        res = 1
        for i in nums:
            mx = max(mx, i)
            mn = min(mn, i)
            if mx-mn>k:
                mx = mn = i
                res+=1
        return res