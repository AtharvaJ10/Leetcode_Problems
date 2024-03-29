# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, target, path):
            if not node:
                return
            
            target-=node.val
            path+=[node.val]
            if target==0 and not node.left and not node.right:
                res.append(path.copy())
            else:
                dfs(node.left, target, path)
                dfs(node.right, target, path)
            path.pop()
        res = []
        dfs(root, targetSum, [])
        return res