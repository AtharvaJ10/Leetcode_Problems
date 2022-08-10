# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        
        res = None
        carry = 0
        while l1 or l2:
            if not l1:
                sum1 = l2.val+carry
                l2 = l2.next
            elif not l2:
                sum1 = l1.val + carry
                l1 = l1.next
            else:
                sum1 = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
                
            if sum1>9:
                sum1-=10
                carry = 1
            else:
                carry = 0
            
            temp = ListNode(sum1)
            temp.next = res
            res = temp
        if carry:
            temp = ListNode(1)
            temp.next = res
            res = temp
        return res
    
    def reverse(self, head):
        prev = None
        while head:
            next1 = head.next
            head.next = prev
            prev = head
            head = next1
        return prev