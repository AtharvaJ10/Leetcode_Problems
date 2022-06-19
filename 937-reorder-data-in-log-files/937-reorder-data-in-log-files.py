class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        """letters,digits= [],[]
        for i in logs:
            if i[-1].isdigit():
                digits.append(i)
            else:
                letters.append(i)
        letters = sorted(letters, key = lambda row: (row.split()[1:], row.split()[0]))
        return letters+digits"""
        
        def custom_sort(log):
            left, right = log.split(" ",1)
            if right[0].isdigit():
                return (1,)
            else:
                return (0, right, left)
        return sorted(logs, key = lambda l: custom_sort(l))