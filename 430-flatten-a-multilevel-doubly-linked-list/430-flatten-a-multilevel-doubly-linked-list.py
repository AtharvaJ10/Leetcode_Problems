"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        stack = [head]
        prev = Node(0)
        while stack:
            root = stack.pop()
            prev.next = root
            root.prev = prev
            prev = root
            if root.next:
                stack.append(root.next)
            if root.child:
                stack.append(root.child)
                root.child = None
        head.prev = None
        return head