# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return (self.bst(nums,0,len(nums)))
    
    def bst(self,nums,low,high):
        if low==high:
            return None
        mid = (low+high)//2
        node = TreeNode(val = nums[mid])
        node.left = self.bst(nums,low,mid)
        node.right = self.bst(nums,mid+1,high)
        return node
        