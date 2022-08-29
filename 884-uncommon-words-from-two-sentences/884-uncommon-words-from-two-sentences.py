class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = Counter(s1.split(" "))
        s2 = Counter(s2.split(" "))
        res = []
        for i in s1:
            if s1[i]==1 and i not in s2:
                res.append(i)
        for i in s2:
            if s2[i]==1 and i not in s1:
                res.append(i)
        return res
        