# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None:
            return False
        
        prev = ListNode(0)
        prev.next = head
        one = prev
        two = head
        
        while(two!=None and two.next!=None):
            if one==two:
                return True
            one = one.next
            two = two.next.next
        return False