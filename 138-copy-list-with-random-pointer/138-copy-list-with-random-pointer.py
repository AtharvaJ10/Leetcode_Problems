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
        d = {}
        prev, curr = None, head
        res = None
        while curr:
            if curr not in d:
                d[curr] = Node(curr.val, curr.next, curr.random)
            if prev:
                prev.next = d[curr]
            else:
                res = d[curr]
            if curr.random:
                if curr.random not in d:
                    d[curr.random] = Node(curr.random.val, curr.random.next, curr.random.random)
                d[curr].random = d[curr.random]
                
            prev,curr = d[curr],curr.next
        return res