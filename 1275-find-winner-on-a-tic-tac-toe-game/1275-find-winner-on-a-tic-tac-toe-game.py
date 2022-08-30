class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [0]*3
        cols = [0]*3
        d1,d2 = 0,0
        
        for i in range(len(moves)):
            if i%2==0:
                rows[moves[i][0]]+=1
                cols[moves[i][1]]+=1
                if moves[i][0]==moves[i][1]:
                    d1+=1
                if moves[i][0]+moves[i][1]==2:
                    d2+=1
            else:
                rows[moves[i][0]]-=1
                cols[moves[i][1]]-=1
                if moves[i][0]==moves[i][1]:
                    d1-=1
                if moves[i][0]+moves[i][1]==2:
                    d2-=1
            
            if 3 in (rows[moves[i][0]], cols[moves[i][1]], d1, d2):
                return "A"
            elif -3 in (rows[moves[i][0]], cols[moves[i][1]], d1, d2):
                return "B"
        return "Pending" if len(moves)<9 else "Draw"