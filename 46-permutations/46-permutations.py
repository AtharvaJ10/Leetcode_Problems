class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.helper(set(), nums, [], [])
    
    def helper(self, set1, nums, res, path):
        if len(path)==len(nums):
            res.append(path)
            return
        
        for i in range(len(nums)):
            if nums[i] in set1:
                continue
            set1.add(nums[i])
            self.helper(set1, nums, res, path+[nums[i]])
            set1.discard(nums[i])
        return res