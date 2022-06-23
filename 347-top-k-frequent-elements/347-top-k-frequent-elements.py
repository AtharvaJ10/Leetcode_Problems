from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        res = []
        for i in nums:
            d[i]+=1
        
        for i in d:
            if len(res)==k:
                heapq.heappushpop(res,(d[i],i))
            else:
                heapq.heappush(res,(d[i],i))
        
        for i in range(len(res)):
            res[i] = res[i][1]
        return res