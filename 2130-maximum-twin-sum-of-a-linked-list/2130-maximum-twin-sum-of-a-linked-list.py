# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast = head, head.next
        while fast.next!= None:
            fast = fast.next.next
            slow = slow.next
        
        temp = slow
        slow = slow.next
        temp.next = None
        while slow!=None:
            next1 = slow.next
            slow.next = temp
            temp = slow
            slow = next1
        
        max1 = 0
        while head!=None:
            max1 = max(max1, head.val+temp.val)
            head = head.next
            temp = temp.next
        return max1