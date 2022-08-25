"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur, prev, d = head, None, {}
        while cur:
            if cur not in d:
                d[cur] = Node(cur.val, cur.next, cur.random)
            if prev:
                prev.next = d[cur]
            else:
                head = d[cur]
            if cur.random:
                if cur.random not in d:
                    d[cur.random] = Node(cur.random.val, cur.random.next, cur.random.random)
                d[cur].random = d[cur.random]
            prev,cur = d[cur], cur.next
        return head