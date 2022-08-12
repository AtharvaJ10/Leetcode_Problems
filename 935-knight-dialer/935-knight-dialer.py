class Solution:
    def knightDialer(self, n: int) -> int:
        paths = {-1:[0,1,2,3,4,5,6,7,8,9], 0: [4,6], 1: [6,8], 2: [7,9], 3: [4,8], 4:[0,3,9], 5:[], 6:[0,1,7], 7:[2,6], 8:[1,3], 9:[2,4]}
        return self.helper(paths, n, -1, {}) % ((10**9)+7)
    
    def helper(self, paths, steps, curr, cache):
        if (steps, curr) in cache:
            return cache[(steps, curr)]
        
        if steps==0:
            return 1
        
        count = 0
        for num in paths[curr]:
            count+=self.helper(paths, steps-1, num, cache)
        
        cache[(steps, curr)] = count
        return count