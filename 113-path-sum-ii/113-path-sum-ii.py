# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, path, target):
            if not node:
                return None
            target-=node.val
            path.append(node.val)
            if target==0 and not node.left and not node.right:
                res.append(path.copy())
            else:
                dfs(node.left, path, target)
                dfs(node.right, path, target)
            path.pop()
        
        res = []
        dfs(root, [], targetSum)
        return res