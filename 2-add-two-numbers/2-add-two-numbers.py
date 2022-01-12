# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode()
        head = result
        carry = 0
        while l1 is not None or l2 is not None:
            #print(result.val)
            if l1==None:
                result.next = ListNode(val = l2.val+carry)
                l2 = l2.next
            elif l2==None:
                result.next = ListNode(val = l1.val+carry)
                l1 = l1.next
            else:
                result.next = ListNode(val = l1.val+l2.val+carry)
                l1 = l1.next
                l2 = l2.next
            
            result = result.next
            if result.val>=10:
                result.val-=10
                carry = 1
            else:
                carry = 0
        
        if carry==1:
            result.next = ListNode(val = carry)
        return head.next