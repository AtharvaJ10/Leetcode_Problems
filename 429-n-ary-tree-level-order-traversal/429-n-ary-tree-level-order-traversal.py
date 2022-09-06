"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = deque([])
        queue.append(root)
        res = []
        while queue:
            level = deque([])
            temp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                for child in node.children:
                    level.append(child)
            res.append(temp)
            queue = level
        return res
            