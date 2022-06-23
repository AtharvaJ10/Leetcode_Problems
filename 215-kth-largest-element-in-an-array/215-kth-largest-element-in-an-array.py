import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """res = []
        for i in nums:
            if len(res)==k:
                heapq.heappushpop(res,i)
            else:
                heapq.heappush(res,i)
        return res[0]"""
        
        res = []
        for i in nums:
            heapq.heappush(res,-i)
        for i in range(k-1):
            heapq.heappop(res)
        return -res[0]
                