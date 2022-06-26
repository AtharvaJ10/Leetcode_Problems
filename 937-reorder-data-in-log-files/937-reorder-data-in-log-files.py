class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def solve(log):
            if log[-1].isdigit():
                return (1,)
            else:
                left, right = log.split(" ",1)
                return (0, right, left)
        
        return sorted(logs, key = solve)