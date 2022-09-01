class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = {"2":'abc',"3":'def',"4":'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = []
        self.helper(0, digits, d, "", res)
        return res
    
    def helper(self, index, digits, d, cur, res):
        if len(cur)==len(digits):
            res.append(cur)
            return
        
        for i in d[digits[index]]:
            self.helper(index+1, digits, d, cur+i, res)
            