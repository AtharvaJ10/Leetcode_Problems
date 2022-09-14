class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = [i+1 for i in range(n)]
        start = 0
        while len(circle)>1:
            start = (start+k-1)%len(circle)
            circle.pop(start)
        return circle[0]