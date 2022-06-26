class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.suggestions = []
        
class Trie:
    def __init__(self):
        self.root = Node(None)
        
    def insert(self, product):
        root = self.root
        for i in product:
            if i not in root.children:
                root.children[i] = Node(i)
            root = root.children[i]
            if len(root.suggestions)<3:
                root.suggestions.append(product)
    
    def find(self, word):
        root = self.root
        res = []
        for i in word:
            if i in root.children:
                root = root.children[i]
                res.append(root.suggestions)
            else:
                break
        rem = len(word) - len(res)
        for i in range(rem):
            res.append([])
        return res
            

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        t = Trie()
        for i in products:
            t.insert(i)
        return t.find(searchWord)