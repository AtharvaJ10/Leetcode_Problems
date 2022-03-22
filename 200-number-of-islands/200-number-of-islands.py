class Solution:
    def dfs(self,grid,i,j,visited):
        if i<0 or j<0 or i>len(grid)-1 or j>len(grid[0])-1 or grid[i][j]=='0' or visited[i][j]:
            return
        visited[i][j] = True
        self.dfs(grid,i+1,j,visited)
        self.dfs(grid,i,j-1,visited)
        self.dfs(grid,i-1,j,visited)
        self.dfs(grid,i,j+1,visited)
        
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        visited = [[False for i in range(len(grid[0]))]for j in range(len(grid))]
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j]=='1':
                    self.dfs(grid,i,j,visited)
                    count+=1
        return count