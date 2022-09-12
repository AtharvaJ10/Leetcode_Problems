"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root or not root.left and not root.right:
            return root
        
        queue = deque([])
        queue.append(root)
        
        while queue:
            level = deque([])
            for i in range(len(queue)):
                node = queue[i]
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            
            for i in range(1, len(queue)):
                queue[i-1].next = queue[i]
            
            queue = level
        return root
            