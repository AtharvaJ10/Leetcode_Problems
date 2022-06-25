class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        memo = {}
        
        def dfs(word):
            if word in memo:
                return memo[word]
            memo[word] = False
            for i in range(1, len(word)):
                if word[:i] in words and (word[i:] in words or dfs(word[i:])):
                    memo[word] = True
                    break
            return memo[word]

        return [word for word in words if dfs(word)]