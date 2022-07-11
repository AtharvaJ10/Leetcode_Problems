import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        res, c = [], Counter(s)
        pq = [[-value,key] for key, value in c.items()]
        heapq.heapify(pq)
        
        prev_value, prev_key = 0, ""
        while pq:
            curr_value, curr_key = heapq.heappop(pq)
            if prev_value<0:
                heapq.heappush(pq, [prev_value, prev_key])
            
            res.append(curr_key)
            curr_value+=1
            prev_value, prev_key = curr_value, curr_key
        if len(res)!=len(s):
            return ""
        return ''.join(res)
            