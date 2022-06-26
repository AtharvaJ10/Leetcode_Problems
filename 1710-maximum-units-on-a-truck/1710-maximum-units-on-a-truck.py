from collections import defaultdict
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        d = defaultdict(int)
        max1 = 0
        for i in boxTypes:
            d[i[1]]+= i[0]
            max1 = max(max1, i[1])
        
        units = 0
        while max1>0:
            if d[max1]>0:
                fit = min(truckSize, d[max1])
                units+= fit*max1
                truckSize-=fit
                if truckSize==0:
                    return units
            max1-=1
        return units
                
        