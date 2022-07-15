from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        current, max_area = 0,0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    queue = deque([])
                    queue.append([i,j])
                    current = 1
                    grid[i][j] = 0
                    while queue:
                        k,l = queue.popleft()
                        for x,y in [k+1,l], [k,l-1], [k-1,l], [k,l+1]:
                            if 0<=x<rows and 0<=y<cols and grid[x][y]==1:
                                grid[x][y] = 0
                                queue.append([x,y])
                                current+=1
                    max_area = max(current, max_area)
        return max_area