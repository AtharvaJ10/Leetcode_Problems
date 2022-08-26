# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(root):
            if not root:
                return 0
            leftsteps = dfs(root.left)
            rightsteps = dfs(root.right)
            self.ans+=abs(leftsteps)+abs(rightsteps)
            return root.val+leftsteps+rightsteps-1
        dfs(root)
        return self.ans