import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        d = Counter(s)
        pkey, pval = "",0
        res = ""
        heap = [(-value, key) for key,value in d.items()]
        heapq.heapify(heap)
        while heap:
            cval, ckey = heapq.heappop(heap)
            if pval:
                heapq.heappush(heap, (pval,pkey))
            res+=ckey
            cval+=1
            pkey,pval = ckey,cval
        return res if len(res)==len(s) else ""