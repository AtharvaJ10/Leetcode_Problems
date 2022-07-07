from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """def dfs(i,j):
            if i<0 or i>=rows or j<0 or j>=cols or visited[i][j] or grid[i][j]=="0":
                return
            visited[i][j] = True
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i-1,j)
            dfs(i,j+1)
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j]=="1":
                    dfs(i,j)
                    count+=1
        return count"""
        
        rows, cols, count = len(grid), len(grid[0]), 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    queue = deque([])
                    queue.append([i,j])
                    grid[i][j] = 0
                    count+=1
                    while queue:
                        k,l = queue.popleft()
                        for x,y in [k+1,l], [k,l-1], [k-1,l], [k,l+1]:
                            if 0<=x<rows and 0<=y<cols and grid[x][y]=="1":
                                queue.append([x,y])
                                grid[x][y] = 0
        return count
                                
        
                    
            