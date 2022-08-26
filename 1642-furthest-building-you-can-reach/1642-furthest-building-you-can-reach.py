import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights)-1):
            dist = heights[i+1]-heights[i]
            if dist<0:
                continue
            heapq.heappush(heap, dist)
            if len(heap)>ladders:
                bricks-=heapq.heappop(heap)
            if bricks<0:
                return i
        return len(heights)-1