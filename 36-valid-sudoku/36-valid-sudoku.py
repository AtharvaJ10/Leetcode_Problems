class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        set1 = set()
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j]!='.':
                    cur = board[i][j]
                    if (i,cur) in set1 or (cur,j) in set1 or (i//3,j//3,cur) in set1:
                        return False
                    set1.add((i,cur))
                    set1.add((cur,j))
                    set1.add((i//3,j//3,cur))
        return True