class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.helper(s, wordDict, {})
    
    def helper(self, curr, words, cache):
        if curr in cache:
            return cache[curr]
        
        if not curr:
            return True
        
        for i in range(len(curr)+1):
            if curr[:i] in words:
                if self.helper(curr[i:], words, cache):
                    cache[curr[:i]] = True
                    return True
        cache[curr[:i]] = False
        return False
                