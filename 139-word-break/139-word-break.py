class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.helper(s, set(wordDict), {})
    
        """class Solution:
    def wordBreak(self, s, wordDict):
		dp = [False]*(len(s)+1)
        dp[0] = True
        
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
					dp[i] = True
                    break
                    
        return dp[-1]"""
    
    def helper(self, curr, words, cache):
        if curr in cache:
            return cache[curr]
        
        if not curr:
            return True
        
        cache[curr] = False
        for i in range(1, len(curr)+1):
            if curr[:i] in words and (curr[i:] in words or self.helper(curr[i:], words, cache)):
                cache[curr] = True
                return True
        return False
    
    