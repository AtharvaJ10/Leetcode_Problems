class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        def binary_search(low, target):
            high = len(products)-1
            while low<high:
                mid = (low+high)//2
                if products[mid]<target:
                    low = mid+1
                else:
                    high = mid
            return low
    
        products.sort()
        res= []
        target = ""
        low = 0
        for i in searchWord:
            target+=i
            index = binary_search(low, target)
            temp = []
            for j in range(index, min(index+3, len(products))):
                if products[j].startswith(target):
                    temp.append(products[j])
            res.append(temp)
            low = index
        return res