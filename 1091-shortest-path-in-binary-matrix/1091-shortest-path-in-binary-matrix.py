class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return -1
        queue = deque([])
        queue.append([0,0,1])
        n = len(grid)
        visited = set((0,0))
        while queue:
            i,j,moves = queue.popleft()
            if (i,j)==(n-1,n-1):
                return moves
            for x,y in [i+1,j], [i+1,j-1], [i,j-1], [i-1,j-1], [i-1,j], [i-1,j+1], [i,j+1], [i+1,j+1]:
                if 0<=x<n and 0<=y<n and (x,y) not in visited and grid[x][y]==0: 
                    visited.add((x,y))
                    queue.append([x,y,moves+1])
        return -1