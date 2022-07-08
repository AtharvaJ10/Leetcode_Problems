from collections import defaultdict
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        d = defaultdict(int)
        max1 = 0
        for i in range(len(boxTypes)):
            d[boxTypes[i][1]] += boxTypes[i][0]
            max1 = max(max1, boxTypes[i][1])
        
        res = 0
        while max1>0:
            if max1 in d:
                fit = min(truckSize, d[max1])
                res+= fit*max1
                truckSize-=fit
                if truckSize==0:
                    return res
            max1-=1
        return res