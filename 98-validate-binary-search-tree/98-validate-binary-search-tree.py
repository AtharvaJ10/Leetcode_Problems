# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(lower, root, upper):
            if not root:
                return True
            
            if lower<root.val<upper:
                return dfs(lower, root.left, root.val) and dfs(root.val, root.right, upper)
            else:
                return False
        return dfs(-float('inf'), root, float('inf'))