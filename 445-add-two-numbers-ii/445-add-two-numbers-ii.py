# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def compute(val, carry):
            res = val+carry
            if res>9:
                res-=10
                carry = 1
            else:
                carry = 0
            return (res, carry)
        
        head1 = None
        while l1:
            temp = l1.next
            l1.next = head1
            head1 = l1
            l1 = temp
        
        head2 = None
        while l2:
            temp = l2.next
            l2.next = head2
            head2 = l2
            l2 = temp

        res = None
        carry = 0
        while head1 or head2:
            if not head1:
                val,carry = compute(head2.val,carry)
                node = ListNode(val)
                node.next = res
                res = node
                head2 = head2.next
            elif not head2:
                val,carry = compute(head1.val,carry)
                node = ListNode(val)
                node.next = res
                res = node
                head1 = head1.next
            else:
                val,carry = compute(head1.val+head2.val, carry)
                node = ListNode(val)
                node.next = res
                res = node
                head1 = head1.next
                head2 = head2.next
        if carry:
            node = ListNode(1)
            node.next = res
            res = node
        return res
        