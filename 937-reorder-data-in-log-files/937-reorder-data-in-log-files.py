class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        """letters = []
        digits = []
        
        for i in logs:
            temp = i.split(" ",1)
            if temp[1][-1].isdigit():
                digits.append(i)
            else:
                letters.append(i)
        letters = sorted(letters, key = lambda l: (l.split(" ",1)[1], l.split(" ",1)[0]))
        
        return letters+digits"""
        
        def solve(log):
            if log.split(" ",1)[1][-1].isdigit():
                return (1,)
            else:
                left, right = log.split(" ",1)
                return (0, right, left)
        return sorted(logs, key = solve)