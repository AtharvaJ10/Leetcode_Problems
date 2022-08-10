class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.helper(s, set(wordDict), {})
    
    def helper(self, current, wordDict, cache):
        if current in cache:
            return cache[current]
        
        if not current:
            return [""]
        
        res = []
        for i in range(1, len(current)+1):
            if current[:i] in wordDict:
                for word in self.helper(current[i:], wordDict, cache):
                    res.append(current[:i] + (" " if word else "") + word)
        
        cache[current] = res
        return res