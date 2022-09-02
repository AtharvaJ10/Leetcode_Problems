class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                live = 0
                for x,y in [i-1,j-1],[i-1,j],[i-1,j+1],[i,j+1],[i+1,j+1],[i+1,j],[i+1,j-1],[i,j-1]:
                    if 0<=x<rows and 0<=y<cols:
                        if abs(board[x][y])==1:
                            live+=1
                if board[i][j]==1:
                    if live<2 or live>3:
                        board[i][j] = -1
                else:
                    if live==3:
                        board[i][j]=2
                #print(board,i,j,live)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j]==-1:
                    board[i][j] = 0
                elif board[i][j]==2:
                    board[i][j]=1
        
        