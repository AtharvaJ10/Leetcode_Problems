class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]==0 or visited[i][j]:
                return 0
            visited[i][j] = True
            res = 1 + dfs(i+1,j) + dfs(i,j-1) + dfs(i-1,j) + dfs(i,j+1)
            return res
        
        
        rows, cols = len(grid), len(grid[0])
        res = 0
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i,j))
        return res