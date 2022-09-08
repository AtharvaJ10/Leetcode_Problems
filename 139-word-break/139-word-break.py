class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        return self.dfs(words, s, {})
    
    def dfs(self, words, curr, cache):
        if curr in cache:
            return cache[curr]
        
        if not curr:
            return True
        
        cache[curr] = False
        for i in range(len(curr)+1):
            if curr[:i] in words and (curr[i:] in words or self.dfs(words, curr[i:], cache)):
                cache[curr] = True
                return True
        return False