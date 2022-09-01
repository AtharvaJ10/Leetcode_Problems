class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
        memo, out_board_p = {(row, column): 1}, 0
        # for each step we will create a new dict to record the onboard coordinates and their probabilities.
        for step in range(k):
            next_memo = collections.defaultdict(int)
            for (i, j), prob in memo.items():
                for d in moves:
                    di, dj = i+d[0], j+d[1]
                    # if the next step is on the board, we record it for next step's calculation
                    if 0<=di<n and 0<=dj<n:
                        next_memo[(di,dj)] += prob * 0.125
                    # if the next step is not on the board, we sum it to our accumulate probability of out-board.
                    else:
                        out_board_p += prob * 0.125
            memo = next_memo
        # the on-board prob = 1 - the accumulate out board prob
        return 1-out_board_p