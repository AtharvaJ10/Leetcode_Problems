class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        d, p = {}, preferences
        for x, y in pairs:
            d[x] = set(p[x][:p[x].index(y)])
            d[y] = set(p[y][:p[y].index(x)])
        
        res = 0
        for x in d:
            for u in d[x]:
                if x in d[u]:
                    res += 1
                    break
        return res