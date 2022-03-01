class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        for i in logs:
            if i[-1].isdigit():
                digits.append(i)
            else:
                letters.append(i)
        letters = sorted(letters,key = lambda l: (l.split()[1:],l.split()[0]))
        return letters+digits
        