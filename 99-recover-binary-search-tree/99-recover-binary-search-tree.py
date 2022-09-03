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
        self.first = self.middle = self.last = self.prev = None
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            
            if self.prev and self.prev.val>node.val:
                if self.first:
                    self.last = node
                else:
                    self.first = self.prev
                    self.middle = node
            self.prev = node
            inorder(node.right)
        
        inorder(root)
        if self.last:
            self.first.val, self.last.val = self.last.val, self.first.val
        else:
            self.first.val, self.middle.val = self.middle.val, self.first.val
            