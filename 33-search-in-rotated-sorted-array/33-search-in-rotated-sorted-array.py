class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                return mid
            if nums[low]<=nums[mid]:
                if nums[low]<=target and target<nums[mid]:
                    high = mid
                else:
                    low = mid+1
            else:
                if nums[mid]<target and target<=nums[high]:
                    low = mid+1
                else:
                    high = mid
        return -1