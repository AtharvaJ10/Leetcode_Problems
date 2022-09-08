import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = [(nums[i][0],i,0) for i in range(len(nums))]
        heapq.heapify(heap)
        
        res = [-float('inf'), float('inf')]
        right = max(i[0] for i in heap)
        while heap:
            left,i,j = heapq.heappop(heap)
            if right-left<res[1]-res[0]:
                res=[left,right]
            if j+1>=len(nums[i]):
                return res
            
            v = nums[i][j+1]
            right = max(right, v)
            heapq.heappush(heap, (v,i,j+1))
        return res