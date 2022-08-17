class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(i,j, x):
            if i<0 or i>=rows or j<0 or j>=cols or image[i][j]!=x or visited[i][j]:
                return
            image[i][j] = color
            visited[i][j] = True
            dfs(i+1,j,x)
            dfs(i,j-1,x)
            dfs(i-1,j,x)
            dfs(i,j+1,x)
        
        rows, cols = len(image), len(image[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        dfs(sr,sc, image[sr][sc])
        return image