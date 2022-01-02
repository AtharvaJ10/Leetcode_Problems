# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursion(self,root):
        if root == None:
            return
        else:
            self.recursion(root.left)
            self.l.append(root.val)
            self.recursion(root.right)
        
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.l = []
        self.recursion(root)
        return self.l
        