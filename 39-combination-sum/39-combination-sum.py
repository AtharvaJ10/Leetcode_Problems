class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.helper(0, candidates, target, [], 0, [])
    
    def helper(self, index, candidates, target, res, cur, path):
        if cur>target:
            return
        if cur==target:
            res.append(path)
            return
        
        for i in range(index, len(candidates)):
            self.helper(i, candidates, target, res, cur+candidates[i], path+[candidates[i]])
        
        return res