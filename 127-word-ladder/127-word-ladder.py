from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque([])
        queue.append([beginWord, 1])
        letters = 'abcdefghijklmnopqrstuvwxyz'
        words = set(wordList)
        while queue:
            word, length = queue.popleft()
            if word==endWord:
                return length
            for i in range(len(word)):
                for c in letters:
                    temp = word[:i] + c + word[i+1:]
                    if temp in words:
                        words.remove(temp)
                        queue.append([temp, length+1])
        return 0