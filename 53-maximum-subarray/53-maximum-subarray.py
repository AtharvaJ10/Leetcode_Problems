class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_max, global_max = -10**4,-10**4
        for i in nums:
            local_max = int(max(i, i + local_max))
            global_max = int(max(local_max, global_max))
        return global_max