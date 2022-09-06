class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(i,j,visited):
            if i<0 or i>=rows or j<0 or j>=cols or (i,j) in visited:
                return
            
            visited.add((i,j))
            for x,y in [i+1,j], [i,j-1],[i-1,j],[i,j+1]:
                if 0<=x<rows and 0<=y<cols:
                    if heights[x][y]>=heights[i][j]:
                        dfs(x,y,visited)
        
        pvisited = set()
        avisited = set()
        rows, cols = len(heights), len(heights[0])
        
        for row in range(rows):
            dfs(row,0,pvisited)
            dfs(row,cols-1,avisited)
            
        for col in range(cols):
            dfs(0,col,pvisited)
            dfs(rows-1,col,avisited)
            
        return list(pvisited & avisited)
        
        