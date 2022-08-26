from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return -1
        elif len(grid)==len(grid[0])==1 and grid[0][0]==0:
            return 1
        rows, cols = len(grid), len(grid[0])
        queue = deque([])
        queue.append([0,0,1])
        while queue:
            i,j,steps = queue.popleft()
            grid[i][j] == 1
            for x,y in [i+1,j+1], [i+1,j], [i+1,j-1], [i,j-1], [i-1,j-1], [i-1,j], [i-1,j+1], [i,j+1]:
                if 0<=x<rows and 0<=y<cols and grid[x][y]==0:
                    if [x,y]==[rows-1,cols-1]:
                        return steps+1
                    grid[x][y] = 1
                    queue.append([x,y,steps+1])
        return -1