class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        def binary_search(low, target):
            hi = len(products)-1
            while low<hi:
                mid = (low+hi)//2
                if products[mid]<target:
                    low = mid+1
                else:
                    hi = mid
            return low
        
        products.sort()
        temp = ""
        res = []
        low = 0
        for i in searchWord:
            temp+=i
            index = binary_search(low, temp)
            low = index
            array = []
            for j in range(index, min(index+3, len(products))):
                if products[j].startswith(temp):
                    array.append(products[j])
            res.append(array)
        return res