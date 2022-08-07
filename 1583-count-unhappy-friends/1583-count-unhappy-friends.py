class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        """Create dictionary using each friend as keys and a list of people they are closer to than the person they are paired with as values. This can be done using index.

Then use nested for loop to find when people are on each other's list."""
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