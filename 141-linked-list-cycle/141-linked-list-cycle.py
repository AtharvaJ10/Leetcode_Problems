# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None:
            return False
        
        a = head.next
        
        while(a!=head):
            if a==None or a.next==None:
                return False
            head = head.next
            a = a.next.next
        return True