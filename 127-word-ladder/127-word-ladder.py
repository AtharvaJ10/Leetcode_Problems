class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque([])
        queue.append([beginWord, 1])
        letters = 'abcdefghijklmnopqrstuvwxyz'
        words = set(wordList)
        while queue:
            word, step = queue.popleft()
            if word==endWord:
                return step
            for i in range(len(word)):
                for c in letters:
                    temp = word[:i] + c + word[i+1:]
                    if temp in words:
                        words.discard(temp)
                        queue.append([temp, step+1])
        return 0