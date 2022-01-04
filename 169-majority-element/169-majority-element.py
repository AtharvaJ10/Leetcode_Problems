class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Moore voting algo
        res = nums[0]
        count = 0
        for i in range(1,len(nums)):
            if nums[i]!=res and count==0:
                res= nums[i]
                count = 0
            elif nums[i]!=res and count>0:
                count-=1
            else:
                count+=1
        return res
                