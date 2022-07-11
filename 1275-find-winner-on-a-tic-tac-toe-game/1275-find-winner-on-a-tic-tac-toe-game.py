class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        row = [[0 for _ in range(3)] for j in range(2)]
        col = [[0 for _ in range(3)] for j in range(2)]
        d1 = [0 for i in range(2)]
        d2 = [0 for i in range(2)]
        id = 0
        for i in moves:
            row[id][i[0]]+=1
            col[id][i[1]]+=1
            
            if i[0]+i[1] == 2:
                d1[id]+=1
            if i[0] == i[1]:
                d2[id]+=1
            
            if 3 in (row[id][i[0]], col[id][i[1]], d1[id], d2[id]):
                return "A" if id%2==0 else "B"
            id+=1
            id%=2
        return 'Draw' if len(moves) == 9 else 'Pending'
            