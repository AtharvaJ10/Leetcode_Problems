from collections import defaultdict
class Node:
    def __init__(self,value):
        self.value = value
        self.children = {}
        self.suggestions = []

class Solution:
    """def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        str1 = ''
        res = []
        for i in searchWord:
            str1+=i
            index = self.binary_search(products,str1)
            temp = []
            for j in range(index, min(index+3,len(products))):
                if products[j].startswith(str1):
                    temp.append(products[j])
            res.append(temp)
        return res
    
    def binary_search(self,products,target):
        low,high = 0,len(products)-1
        while low<high:
            mid = (low+high)//2
            if products[mid]<target:
                low = mid+1
            else:
                high = mid
        return low"""
    
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
                res.append(root.children[i].suggestions)
                root = root.children[i]
            else:
                break
        remaining = len(word) - len(res)
        for i in range(remaining):
            res.append([])
        return res
        
        
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        products.sort()
        for product in products:
            self.insert(product)
        
        return (self.find(searchWord))