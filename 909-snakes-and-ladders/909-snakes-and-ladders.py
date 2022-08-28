from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def get_index(square):
            r,c = divmod(square-1, n)
            if r%2!=0:
                return n-r-1, n-c-1
            else:
                return n-r-1, c
        
        n = len(board)
        queue = deque([])
        queue.append([1,0])
        visited = set()
        while queue:
            square, steps = queue.popleft()
            r,c = get_index(square)
            if board[r][c]!=-1:
                square = board[r][c]
            if square==n*n:
                return steps
        
            for i in range(1,7):
                if square+i<=n*n and square+i not in visited:
                    visited.add(square+i)
                    queue.append([square+i, steps+1])
        return -1