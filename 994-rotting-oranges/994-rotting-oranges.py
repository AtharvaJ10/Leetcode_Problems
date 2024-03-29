class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rows,cols = len(grid), len(grid[0])
        queue = deque([])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    queue.append([i,j,0])
        
        if fresh==0:
            return 0
        
        while queue:
            r,c,minutes = queue.popleft()
            for x,y in [r+1,c], [r,c-1], [r-1,c], [r,c+1]:
                if 0<=x<rows and 0<=y<cols and grid[x][y]==1:
                    fresh-=1
                    if fresh==0:
                        return minutes+1
                    grid[x][y]=0
                    queue.append([x,y,minutes+1])
                    
        if fresh:
            return -1
        else:
            return 0
                    