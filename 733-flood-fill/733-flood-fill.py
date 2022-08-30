class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = deque([])
        queue.append([sr,sc])
        comp = image[sr][sc]
        image[sr][sc] = color
        visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]
        visited[sr][sc] = True
        while queue:
            r,c = queue.popleft()
            for i,j in [r+1,c], [r,c-1], [r-1,c], [r,c+1]:
                if 0<=i<len(image) and 0<=j<len(image[0]) and image[i][j]==comp and not visited[i][j]:
                    image[i][j] = color
                    queue.append([i,j])
                    visited[i][j] = True
        return image