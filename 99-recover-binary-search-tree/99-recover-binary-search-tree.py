# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = self.prev = self.middle = self.last = None
        
        def dfs(node):
            if node:
                dfs(node.left)
                if self.prev is not None and self.prev.val>node.val:
                    if self.first is None:
                        self.first = self.prev
                        self.middle = node
                    else:
                        self.last = node
                self.prev = node
                dfs(node.right)
        
        dfs(root)
        if self.last is not None:
            self.first.val, self.last.val = self.last.val, self.first.val
        else:
            self.first.val, self.middle.val = self.middle.val, self.first.val