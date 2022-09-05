class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        queue = defaultdict(int)
        queue[(row,column)] = 1
        out_prob = 0
        dirs = [[-2,-1], [-1,-2],[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1]]
        for _ in range(k):
            layer = defaultdict(int)
            for (r,c),prob in queue.items():
                for i,j in dirs:
                    x,y = r+i, c+j
                    if 0<=x<n and 0<=y<n:
                        layer[(x,y)]+=prob*0.125
                    else:
                        out_prob+=prob*0.125
            queue = layer
        return 1-out_prob
                
                