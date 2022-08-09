# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev1 = None
        while l1:
            next1 = l1.next
            l1.next = prev1
            prev1 = l1
            l1 = next1
        
        prev2 = None
        while l2:
            next1 = l2.next
            l2.next = prev2
            prev2 = l2
            l2 = next1
        
        res, carry = 0,0
        prev = None
        l1, l2 = prev1, prev2
        
        while l1 or l2:
            if not l1:
                res=l2.val+carry
                l2 = l2.next
            elif not l2:
                res=l1.val+carry
                l1 = l1.next
            else:
                res=l1.val+l2.val+carry
                l1 = l1.next
                l2 = l2.next
            if res>9:
                res-=10
                carry = 1
            else:
                carry = 0
            next1 = ListNode(res)
            next1.next = prev
            prev = next1
        if carry==1:
            next1 = ListNode(1)
            next1.next = prev
            prev = next1
        return prev