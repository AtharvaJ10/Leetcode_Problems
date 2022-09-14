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
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = deque([])
        queue.append(root)
        
        while queue:
            level = deque([])
            for i in range(len(queue)):
                node = queue[i]
                if i==len(queue)-1:
                    node.next = None
                else:
                    node.next = queue[i+1]
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            queue = level
        return root