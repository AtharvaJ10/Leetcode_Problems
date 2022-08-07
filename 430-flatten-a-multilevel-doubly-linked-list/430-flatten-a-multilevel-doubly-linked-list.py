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
        def dfs(head):
            cur = prev = head
            while cur:
                if cur.child:
                    cur.child.prev = cur
                    cur_next = cur.next
                    cur.next = cur.child
                    cur.child = None
                    cur = dfs(cur.next)
                    cur.next = cur_next
                    if cur.next:
                        cur.next.prev = cur
                cur,prev = cur.next, cur
            return prev
        dfs(head)
        return head
                        