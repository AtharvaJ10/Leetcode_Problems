class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.dfs(s, set(wordDict), {})
    
    def dfs(self, s, words, cache):
        if s in cache:
            return cache[s]
        if not s:
            return [""]
        
        res = []
        for i in range(1, len(s)+1):
            if s[:i] in words:
                for word in self.dfs(s[i:], words, cache):
                    res.append(s[:i] + (" " if word else "") + word)
        
        cache[s] = res
        return res
                    