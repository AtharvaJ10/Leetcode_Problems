class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {"2":'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        return self.helper(d, digits, [], "", 0)
    
    def helper(self, d, digits, res, path, ind):
        if ind==len(digits):
            res.append(path)
            return
        
        for char in d[digits[ind]]:
            self.helper(d, digits, res, path+char, ind+1)
        
        return res