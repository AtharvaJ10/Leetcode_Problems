class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        for i in logs:
            if i[-1].isdigit():
                digits.append(i)
            else:
                letters.append(i)
        letters = sorted(letters,key = lambda l: (l.split(" ",1)[1],l.split(" ",1)[0]))
        return letters+digits
        
        """def sorting_algo(log):
            left, right = log.split(" ",1)
            if right[0].isalpha():
                return (0,right,left)
            else:
                return (1,)
        return sorted(logs, key = sorting_algo)"""
        