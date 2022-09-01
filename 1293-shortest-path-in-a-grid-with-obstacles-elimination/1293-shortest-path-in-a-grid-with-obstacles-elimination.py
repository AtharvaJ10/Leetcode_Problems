class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows,cols = len(grid), len(grid[0])
        if k >= rows + cols - 2: return rows + cols - 2  # if we can go by manhattan distance -> let's go
        queue = deque([])
        queue.append([0,0,k,0])
        visited = set()
        visited.add((0,0,k))
        while queue:
            i,j,k,step = queue.popleft()
            if (i,j)==(rows-1,cols-1):
                return step
            
            for x,y in [i+1,j], [i,j-1], [i-1,j], [i,j+1]:
                if 0<=x<rows and 0<=y<cols:
                    new_k = k-grid[x][y]
                    if new_k>=0 and (x,y,new_k) not in visited:
                        visited.add((x,y,new_k))
                        queue.append([x,y,new_k, step+1])
        return -1