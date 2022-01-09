# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next==None:
            return True       
        
        slow = head
        fast = head
        prev = None
        
        while fast!=None and fast.next!= None:
            #print(fast.val,fast.next.val,fast.next.next.val)
            fast = fast.next.next
    
            next1 = slow.next
            slow.next = prev
            prev = slow
            slow = next1
            
        if fast!=None:
            slow = slow.next
            
        while slow!=None:
            if slow.val !=prev.val:
                return False
            slow = slow.next
            prev = prev.next
            
        return True
            
        
        
            
            