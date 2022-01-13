class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points)==1:
            return 1
        points.sort(key = lambda row: row[1])
        i,j = 0,1
        count = 0
        print(points)
        while j<len(points):
            #print(i,j,points[i],points[j])
            count+=1
            while j<len(points) and points[i][1]>=points[j][0] and points[i][1]<=points[j][1]:
                j+=1
            
            if j==len(points)-1:
                count+=1
                break
            else:
                i = j
                j+=1          
        return count
            
        