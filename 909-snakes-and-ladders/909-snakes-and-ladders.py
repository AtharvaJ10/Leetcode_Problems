from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def compute(square):
            r,c = divmod(square-1, len(board))
            if r%2!=0:
                return n-r-1, n-c-1
            else:
                return n-r-1, c
        
        queue = deque([])
        queue.append([1,0])
        visited = set()
        n = len(board)
        while queue:
            square, step = queue.popleft()
            r,c = compute(square)
            if board[r][c]!=-1:
                square = board[r][c]
            if square == len(board)**2:
                return step
            for i in range(1, 7):
                new_square= square + i
                if new_square <= len(board)**2 and new_square not in visited:
                    visited.add(new_square)
                    queue.append([new_square, step+1])
        return -1
        