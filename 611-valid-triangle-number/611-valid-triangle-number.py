class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        k = 2
        while k<len(nums):
            i = 0
            j = k-1
            while j>i:
                if nums[i]+nums[j]>nums[k]:
                    res+=j-i
                    j-=1
                else:
                    i+=1  
            k+=1
        return res
            