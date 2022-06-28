# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(head.val, i, head) for i,head in enumerate(lists) if head]
        heapify(heap)
        dummy = ListNode(0)
        curr = dummy
        while heap != []:
            val, i, node = heap[0]
            if not node.next: # exhausted one linked-list
                heappop(heap)
            else:
                heapreplace(heap, (node.next.val, i, node.next)) # recycling tie-breaker i guarantees uniqueness
            curr.next = node    
            curr = curr.next
        return dummy.next