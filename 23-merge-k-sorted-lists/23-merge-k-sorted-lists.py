# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(head.val, i, head) for i,head in enumerate(lists) if head]
        result = ListNode()
        temp = result
        
        heapq.heapify(heap)
        while heap!=[]:
            val, index, node = heap[0]
            if not node.next:
                heapq.heappop(heap)
            else:
                heapq.heapreplace(heap, (node.next.val, index, node.next))
            temp.next = node
            temp = temp.next
        return result.next