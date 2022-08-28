class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {2: 'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        return self.helper(digits, 0, d, [], '')
    
    def helper(self, digits, ind, d, res, path):
        if ind==len(digits):
            res.append(path)
            return
        
        for i in d[int(digits[ind])]:
            self.helper(digits, ind+1, d, res, path+i)        
        return res
            