# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next==None:
            return True       
        
        length = 0
        temp = head
        
        while temp!=None:
            length+=1
            temp = temp.next
        
        prev = None
        temp = head
        total = length
            
        total = total//2
        while total!= 0:
            next1 = temp.next
            temp.next = prev
            prev = temp
            temp = next1
            total-=1
        
        if length%2 == 1:
            temp = temp.next
            
        while temp!=None:
            if temp.val!=prev.val:
                return False
            else:
                temp = temp.next
                prev = prev.next
        return True
            
            