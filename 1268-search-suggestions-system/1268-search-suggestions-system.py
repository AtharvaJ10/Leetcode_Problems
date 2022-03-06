class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        res = []
        for i in range(len(searchWord)):
            temp = []
            for j in range(len(products)):
                if searchWord[:i+1]==products[j][:i+1]:
                    temp.append(products[j])
            res.append(temp.copy()[:3])
        return res
            
            
        