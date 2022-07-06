class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result, current = 0, 0
        set1 = set(nums)
        for i in set1:
            if i-1 not in set1:
                current = 1
                while i+1 in set1:
                    current+=1
                    i+=1
                result = max(result, current)
        return result