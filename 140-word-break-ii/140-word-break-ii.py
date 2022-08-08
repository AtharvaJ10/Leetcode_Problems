class Solution:
    """def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
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
        return res"""
    
    def wordBreak(self, s, words):
        """40ms, beating 98.4%. Uses DP to determine reachable locations
        in the word, then a DFS to explore paths from the start to the 
        end of the word.
        
        Uses varying string concatenation to add to path.
        """
        result = []
             
        def dfs(dp, end, path):
            """A DFS to add paths that reach from the end of the word
            to the start.
            """
            # If we have reached the start of the word, add to result
            if 0 == end:
                result.append(path)
                return
                
            # Otherwise consider each possible path from the end
            for word in dp[end]:

                # If we already have a word in the path, add a space in between
                if path:
                    dfs(dp, end - len(word), word + " " + path)
                else:
                    dfs(dp, end - len(word), word)
        
        # Used for O(1) lookup
        word_set = set(words)
        
        # Used for limiting the search for substrings (words) ending at each position
        max_len = max([len(w) for w in words + ['']])
        
        # Stores whether a combination of words from `words` can reach the position
        dp = [[] for _ in range(len(s) + 1)]
        dp[0] = True
        
        # Words ending at i
        for i in range(1, len(s) + 1):
            
            # j defines a reachable location & start of a word ending at i
            for j in range(max(0, i - max_len), i):
            
                # If j is a reachable position & j to i defines a dictionary word
                if dp[j] and s[j:i] in word_set:
                    dp[i].append(s[j:i])
    
        # For each word in dp[len(s)], explore if it's possible to reach the start of s.
        # If so, append a joining of the path to our output
        dfs(dp, len(s), "")
        return result
                    