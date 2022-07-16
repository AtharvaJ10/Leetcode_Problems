# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        count, res = 1, []
        queue = []
        queue.append(root)
        while queue:
            length = len(queue)
            if count%2==1:
                res.append([node.val for node in queue])
            else:
                res.append([queue[i].val for i in range(length-1,-1,-1)])
            for i in range(length):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            count+=1
        return res
            
            