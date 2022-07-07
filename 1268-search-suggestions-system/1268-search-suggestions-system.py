class Node:
    def __init__(self, value = None):
        self.value = value
        self.suggestions = []
        self.children = {}
    
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, product):
        temp = self.root
        for j in product:
            if j not in temp.children:
                temp.children[j] = Node(j)
            temp = temp.children[j]

            if len(temp.suggestions)<3:
                temp.suggestions.append(product)
    
    def find(self, target):
        res = []
        temp = self.root
        for i in target:
            if i in temp.children:
                temp = temp.children[i]
                res.append(temp.suggestions)
            else:
                break
        rem = len(target) - len(res)
        for i in range(rem):
            res.append([])
        return res

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for i in products:
            trie.insert(i)
        return trie.find(searchWord)