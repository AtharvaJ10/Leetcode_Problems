class Solution:
    def knightDialer(self, n: int) -> int:
        d = {-1:[0,1,2,3,4,5,6,7,8,9], 0:[4,6], 1:[6,8], 2:[7,9], 3:[4,8], 4:[0,3,9], 5:[], 6:[0,1,7], 7:[2,6], 8:[1,3], 9:[2,4]}
        return self.helper(d, -1, n, {}) %(10**9+7)
    
    def helper(self, d, cur, steps, cache):
        if (cur,steps) in cache:
            return cache[(cur,steps)]
        
        if steps==0:
            return 1
        
        count = 0
        for i in d[cur]:
            count+=self.helper(d, i, steps-1, cache)
            
        cache[(cur, steps)] = count
        return count