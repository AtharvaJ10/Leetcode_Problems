class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def enough(dist):
            i,j,count = 0,0,0
            while i<n or j<n:
                while j<n and nums[j]-nums[i]<=dist:
                    j+=1
                count+=j-i-1
                i+=1
            return count>=k
        
        nums.sort()
        n, low ,hi = len(nums), 0, nums[-1]-nums[0]
        while low<hi:
            print(low, hi)
            mid = (low+hi)//2
            if not enough(mid):
                low = mid + 1
            else:
                hi = mid
            #print(low, hi)
        return low