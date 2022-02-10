import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for i in range(len(points)):
            dist = points[i][0]**2+points[i][1]**2
            temp = [points[i][0],points[i][1]]
            if len(h)<k:
                heapq.heappush(h,(-dist,temp))
            else:
                heapq.heappushpop(h,(-dist,temp))
        return [h[i][1] for i in range(len(h))]