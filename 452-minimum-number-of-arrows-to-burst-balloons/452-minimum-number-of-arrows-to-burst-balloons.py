class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda row: row[1])
        count = 1
        temp = points[0][1]
        for i in range(1,len(points)):
            if temp>=points[i][0]:
                continue
            temp = points[i][1]
            count+=1
        return count
        
            
        