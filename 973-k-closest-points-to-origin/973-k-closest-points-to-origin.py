import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for i in points:
            dist = math.sqrt(i[0]**2 + i[1]**2)
            if len(res)<k:
                heapq.heappush(res, (-dist, i))
            else:
                heapq.heappushpop(res, (-dist,i))
        
        return [i[1] for i in res]
        