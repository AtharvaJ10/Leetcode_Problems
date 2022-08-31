class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def compute(square):
            r,c = divmod(square-1, n)
            if r%2==0:
                return n-r-1, c
            else:
                return n-r-1, n-c-1
        
        queue = deque([])
        queue.append([1,0])
        n = len(board)
        visited = set([1])
        while queue:
            square, steps = queue.popleft()
            r,c = compute(square)
            if board[r][c]!=-1:
                square = board[r][c]
            if square == n**2:
                return steps
            for i in range(1, 7):
                new_square = square+i
                if new_square not in visited and new_square<=n**2:
                    visited.add(new_square)
                    queue.append([new_square, steps+1])
        return -1