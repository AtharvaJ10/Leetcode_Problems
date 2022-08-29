import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = [(nums[i][0], i, 0) for i in range(len(nums))]
        heapq.heapify(heap)
        ans = [-float('inf'), float('inf')]
        right = max(nums[i][0] for i in range(len(nums)))
        while heap:
            left, i, j = heapq.heappop(heap)
            if right-left < ans[1]-ans[0]:
                ans = [left, right]
            if j+1 == len(nums[i]):
                return ans
            v = nums[i][j+1]
            right = max(right, v)
            heapq.heappush(heap, (v,i,j+1))
        return ans