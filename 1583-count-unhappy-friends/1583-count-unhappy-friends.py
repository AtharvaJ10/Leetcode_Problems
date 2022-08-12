class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        d = defaultdict(list)
        for i,j in pairs:
            d[i] = preferences[i][:preferences[i].index(j)]
            d[j] = preferences[j][:preferences[j].index(i)]
        
        count = 0
        for i in d:
            for j in d[i]:
                if i in d[j]:
                    count+=1
                    break
        return count