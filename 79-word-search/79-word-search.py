class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j,x):
            if x==len(word):
                return True
            
            if i<0 or i>=rows or j<0 or j>=cols or visited[i][j] or board[i][j]!=word[x]:
                return False
            
            visited[i][j] = True
            res = dfs(i+1,j,x+1) or dfs(i,j-1,x+1) or dfs(i-1,j,x+1) or dfs(i,j+1,x+1)
            visited[i][j] = False
            return res
        
        rows, cols = len(board), len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        x= 0
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and board[i][j]==word[x]:
                    if dfs(i,j,x):
                        return True
        return False