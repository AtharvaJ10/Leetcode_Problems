class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        t, res = Trie(), []
        for word in words:
            t.add(word)
        for word in words:
            if t.helper(word, 0, len(word) - 1, 0):
                res.append(word)
        return res


class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = Node()
        self.dp = {}

    def add(self, word):
        p = self.root
        for c in word:
            if c not in p.children:
                p.children[c] = Node()
            p = p.children[c]
        p.is_end = True


    def helper(self, word, st, end, cnt):
        p = self.root

        w = word[st:end+1]
        if w in self.dp: return self.dp[w]

        for x in range(st, end + 1):
            if word[x] in p.children:
                p = p.children[word[x]]

                if p.is_end:
                    if x == end:
                        return cnt >= 1

                    if self.helper(word, x + 1, end, cnt + 1):
                        self.dp[w] = True
                        return True
            else:
                break

        self.dp[w] = False
        return False