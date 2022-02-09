from collections import defaultdict
import sys,math
class Solution:
    def distance(self,x,y):
        return math.sqrt(y**2 + x**2)
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = defaultdict(list)
        
        for i in range(len(points)):
            temp = self.distance(points[i][1],points[i][0])
            d[temp].append([points[i][0],points[i][1]])
            
        res = []
        for key in sorted(d.keys()):
            for value in d[key]:
                if len(res)==k:
                    return res
                else:
                    res.append(value)
        return res