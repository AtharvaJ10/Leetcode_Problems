import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        heap,res, d = [],"", Counter(s)
        for i in d:
            heap.append([-d[i],i])
        heapq.heapify(heap)
        
        prev_key, prev_value = 0,0
        while heap:
            curr_value, curr_key = heapq.heappop(heap)
            if prev_value<0:
                heapq.heappush(heap,[prev_value, prev_key])
            res+=curr_key
            curr_value+=1
            prev_value, prev_key = curr_value, curr_key
        
        return res if len(res)==len(s) else ""