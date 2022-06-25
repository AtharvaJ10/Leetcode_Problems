class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        t, memo, res = Trie(), {}, []
        for word in words:
            t.add(word)
        for word in words:
            if t.helper(word, 0, len(word) - 1, 0, memo):
                res.append(word)
        return res


class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        p = self.root
        for c in word:
            if c not in p.children:
                p.children[c] = Node()
            p = p.children[c]
        p.is_end = True


    def helper(self, word, st, end, cnt, memo):
        p = self.root
        curr = word[st: end + 1]
        if curr in memo: 
            return memo[curr]
        
        for x in range(st, end + 1):
            if word[x] in p.children:
                p = p.children[word[x]]
                if p.is_end:
                    if x == end:
                        return cnt >= 1
                    if self.helper(word, x + 1, end, cnt + 1, memo):
                        memo[curr] = True
                        return True
            else:
                break
                
        memo[curr] = False
        return False