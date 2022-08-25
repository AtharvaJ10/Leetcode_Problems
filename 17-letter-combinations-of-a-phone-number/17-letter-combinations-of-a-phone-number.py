class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2': 'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        return self.helper(d, digits, "", 0, [])
    
    def helper(self, d, digits, curr, i, res):
        if i==len(digits):
            res.append(curr)
            return
        
        for j in d[digits[i]]:
            curr+=j
            self.helper(d, digits, curr, i+1, res)
            curr = curr[:-1]
        return res
            
        