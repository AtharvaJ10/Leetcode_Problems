import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        prev_key, prev_val = "", 0
        heap = [(-val, key) for key,val in c.items()]
        heapq.heapify(heap)
        res = ""
        while heap:
            curr_val, curr_key = heapq.heappop(heap)
            if prev_val<0:
                heapq.heappush(heap, (prev_val, prev_key))
            res+=curr_key
            curr_val+=1
            prev_key, prev_val = curr_key, curr_val
        return res if len(res)==len(s) else ""