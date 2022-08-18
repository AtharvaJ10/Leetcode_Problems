class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            temp = list(i)
            temp.sort()
            d[''.join(temp)].append(i)
        
        res = []
        for i in d:
            res.append(d[i])
        return res