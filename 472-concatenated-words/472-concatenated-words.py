class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)
        
        def dfs(word):
            for i in range(1, len(word)):
                prefix, suffix = word[:i], word[i:]
                if prefix in wordSet and (suffix in wordSet or dfs(suffix)):
                    return True
            return False
                    
        return [w for w in words if dfs(w)]