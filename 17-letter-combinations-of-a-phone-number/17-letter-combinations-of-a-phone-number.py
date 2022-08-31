class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2':'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        return self.helper(0, digits, "", d, [])
    
    def helper(self, curr, digits, path, d, res):
        if len(path)==len(digits):
            res.append(path)
            return
    
        for i in d[digits[curr]]:
            self.helper(curr+1, digits, path+i, d, res)
        
        return res