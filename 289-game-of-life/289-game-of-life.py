class Solution:
    def gameOfLife(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                live = 0
                for x,y in [i+1,j], [i+1,j-1], [i,j-1], [i-1,j-1], [i-1,j], [i-1,j+1], [i,j+1], [i+1,j+1]:
                    if 0<=x<rows and 0<=y<cols and abs(grid[x][y])==1:
                        live+=1
                if grid[i][j]==1:
                    if live<2 or live>3:
                        grid[i][j] = -1
                elif grid[i][j]==0:
                    if live==3:
                        grid[i][j] = 2
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==-1:
                    grid[i][j] = 0
                elif grid[i][j]==2:
                    grid[i][j] = 1
                    
                    
        