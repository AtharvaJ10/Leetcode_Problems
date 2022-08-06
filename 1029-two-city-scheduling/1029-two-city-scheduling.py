class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        min_cost = 0
        refund = []
        for a,b in costs:
            min_cost+=a
            refund.append(b-a)
        refund.sort()
        
        for i in range(len(refund)//2):
            min_cost+=refund[i]
        return min_cost