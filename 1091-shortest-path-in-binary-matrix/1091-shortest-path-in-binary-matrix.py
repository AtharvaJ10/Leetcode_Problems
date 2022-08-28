class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return -1
        rows, cols = len(grid), len(grid[0])
        queue = deque([])
        queue.append((0,0,1))
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        visited[0][0] = True
        while queue:
            i,j, steps = queue.popleft()
            if (i,j) == (rows-1,cols-1):
                return steps
            for x,y in [i+1,j+1], [i+1,j], [i+1,j-1], [i,j-1], [i-1,j-1], [i-1,j], [i-1,j+1], [i,j+1]:
                if 0<=x<rows and 0<=y<cols and grid[x][y]==0 and not visited[x][y]:
                    if (x,y) == (rows-1,cols-1):
                        return steps+1
                    visited[x][y] = True
                    queue.append((x,y,steps+1))
        return -1