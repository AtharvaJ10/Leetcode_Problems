class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        queue = deque([])
        queue.append([0,0,0,k])
        rows, cols = len(grid), len(grid[0])
        visited = set()
        visited.add((0,0,k))
        while queue:
            r,c,step,k = queue.popleft()
            if (r,c)==(rows-1,cols-1):
                return step
            
            for x,y in [r+1,c], [r,c-1], [r-1,c], [r,c+1]:
                if 0<=x<rows and 0<=y<cols:
                    new_k=k-grid[x][y]
                    if new_k>=0 and (x,y,new_k) not in visited:
                        visited.add((x,y,new_k))
                        queue.append([x,y,step+1,new_k])
        return -1