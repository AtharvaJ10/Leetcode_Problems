# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursion(self, left, right):
        if left==None and right==None:
            return True
        elif left==None or right==None:
            return False
        elif left.val != right.val:
            return False
        res = self.recursion(left.left,right.right)
        if res:
            res = self.recursion(left.right,right.left)
        else:
            return False
        return res
            
        
        
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left==None and root.right==None:
            return True
        res = self.recursion(root.left,root.right)
        return res
        