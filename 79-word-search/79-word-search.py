from collections import deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j,x):
            if i<0 or i>=rows or j<0 or j>=cols or board[i][j]!=word[x] or x>=len(word) or visited[i][j]:
                return False
            visited[i][j] = True
            if x==len(word)-1:
                return True
            res = dfs(i+1,j,x+1) or dfs(i,j-1,x+1) or dfs(i-1,j,x+1) or dfs(i,j+1,x+1)
            visited[i][j] = False
            return res
        
        rows, cols, flag = len(board), len(board[0]), False
        visited = [[False for _ in range(cols)] for _ in range (rows)]
        for i in range(rows):
            for j in range(cols):
                if board[i][j]==word[0] and not visited[i][j]:
                    if dfs(i,j,0):
                        return True
        return False
                    