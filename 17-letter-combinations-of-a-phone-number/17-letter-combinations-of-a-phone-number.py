class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        return self.helper(digits, d, "", [], 0)
    
    def helper(self, digits, d, path, res, ind):
        if ind>=len(digits):
            res.append(path)
            return
        
        for char in d[digits[ind]]:
            self.helper(digits, d, path+char, res, ind+1)
        
        return res