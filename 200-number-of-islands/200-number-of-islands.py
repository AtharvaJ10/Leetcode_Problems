class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]=="0" or visited[i][j]:
                return
            
            visited[i][j] = True
            dfs(i,j+1)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i-1,j)
        
        count = 0
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j]=="1":
                    dfs(i,j)
                    count+=1
        return count