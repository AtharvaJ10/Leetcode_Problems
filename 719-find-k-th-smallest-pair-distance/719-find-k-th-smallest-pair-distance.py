class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def enough(dist):
            i,j,count = 0,0,0
            while i<len(nums) or j<len(nums):
                while j<len(nums) and nums[j]-nums[i]<=dist:
                    j+=1
                count+=j-i-1
                i+=1
            return count>=k
        
        
        nums.sort()
        low, high = 0, nums[-1]-nums[0]
        while low<high:
            mid = (low+high)//2
            if enough(mid):
                high = mid
            else:
                low = mid+1
        return low