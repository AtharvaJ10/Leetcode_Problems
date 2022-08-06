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
        """if not head:
            return None
        prev = Node(0)
        stack = [head]
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
        return head"""
        
        if not head:
            return None
        def dfs(head):
            curr=prev=head
            while curr:
                if curr.child:
                    curr.child.prev = curr
                    curr_next = curr.next
                    curr.next = curr.child
                    curr.child = None
                    curr = dfs(curr.next)
                    curr.next = curr_next
                    if curr.next:
                        curr.next.prev = curr
                curr,prev = curr.next, curr
            return prev
        dfs(head)
        return head