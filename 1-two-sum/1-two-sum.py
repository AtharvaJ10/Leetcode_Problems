class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            if nums[i] not in d:
                d[target-nums[i]] = i
            else:
                return [i, d[nums[i]]]