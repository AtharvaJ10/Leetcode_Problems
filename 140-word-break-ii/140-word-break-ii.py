class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        return self.helper(s, wordDict, {})
    
    def helper(self, curr, wordDict, cache):
        if curr in cache:
            return cache[curr]
        
        if not curr:
            return [""]
        
        res = []
        for i in range(len(curr)+1):
            if curr[:i] in wordDict:
                #print(curr[:i])
                for word in self.helper(curr[i:], wordDict, cache):
                    res.append(curr[:i] + (" " if word else "") + word)
        
        cache[curr] = res
        return res