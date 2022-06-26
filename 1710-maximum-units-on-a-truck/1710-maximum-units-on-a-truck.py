class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key = lambda l: -l[1])
        count = 0
        units = 0
        for i in boxTypes:
            if count+i[0]<=truckSize:
                units+= i[0]*i[1]
                count+=i[0]
            else:
                rem = truckSize - count
                units+= rem*i[1]
                break
        return units
                