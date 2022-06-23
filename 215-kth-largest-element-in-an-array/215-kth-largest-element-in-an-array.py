import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        for i in nums:
            if len(res)==k:
                heapq.heappushpop(res,i)
            else:
                heapq.heappush(res,i)
        return res[0]
                