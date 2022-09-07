class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, hi = max(weights), sum(weights)
        while low<hi:
            mid = (low+hi)//2
            
            d = 1
            cur = 0
            for w in weights:
                cur+=w
                if cur>mid:
                    cur = w
                    d+=1
            
            if d>days:
                low = mid+1
            else:
                hi = mid
        return low