# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root==None:
            root = TreeNode(val = val)
            return root
    
        temp = root
        while True:
            if temp.left==None and val<temp.val:
                temp.left = TreeNode(val = val)
                break
            if temp.right==None and val>temp.val:
                temp.right = TreeNode(val = val)
                break
                
            if val<temp.val:
                temp = temp.left
            else:
                temp = temp.right
                
        return root
                
                
        