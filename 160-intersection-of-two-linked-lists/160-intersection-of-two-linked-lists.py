# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a,b = headA,headB
        flag = False
        while True:
            if a==b:
                flag = True
                break
            if a==None and b==None:
                break
            if a==None:
                a = headB
            else:
                a = a.next
            if b==None:
                b = headA
            else:
                b = b.next
        if flag:
            return a
        else:
            return None
                
                
        