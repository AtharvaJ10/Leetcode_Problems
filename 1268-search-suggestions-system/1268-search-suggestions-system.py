class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        str1 = ''
        res = []
        for i in searchWord:
            str1+=i
            index = self.binary_search(products,str1)
            temp = []
            for j in range(min(index+3,len(products))):
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
        return low