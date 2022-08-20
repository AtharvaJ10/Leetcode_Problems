import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        heap, res, d = [], "", Counter(s)
        for i in d:
            heap.append((-d[i], i))
        
        heapq.heapify(heap)
        prev_val, prev_key = 0, ""
        while heap:
            curr_val, curr_key = heapq.heappop(heap)
            if prev_val<0:
                heapq.heappush(heap, (prev_val, prev_key))
            res+=curr_key
            curr_val+=1
            prev_key, prev_val = curr_key, curr_val
            
        return res if len(res)==len(s) else ""
            