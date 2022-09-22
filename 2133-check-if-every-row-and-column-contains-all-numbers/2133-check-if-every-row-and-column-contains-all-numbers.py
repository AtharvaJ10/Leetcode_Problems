class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        for row,col in zip(matrix, zip(*matrix)):
            if len(set(row))!=len(matrix) or len(set(col))!=len(matrix):
                return False
        return True