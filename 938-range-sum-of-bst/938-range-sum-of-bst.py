# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue = [root]
        res = 0
        
        while queue:
            node = queue.pop(0)
            print(node.val)
            if node.val>=low and node.val<=high:
                res+=node.val
                if node.val == high and node.left is not None:
                    queue.append(node.left)
                elif node.val == low and node.right is not None:
                    queue.append(node.right)
                else:
                    if node.left is not None:
                        queue.append(node.left)
                    if node.right is not None:
                        queue.append(node.right)
            elif node.val<low and node.right is not None:
                queue.append(node.right)
            elif node.val>high and node.left is not None:
                queue.append(node.left)
        return res
        