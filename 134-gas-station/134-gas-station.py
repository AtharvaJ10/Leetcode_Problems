class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, total, current = 0, 0, 0
        for i in range(len(gas)):
            current += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if current<0:
                current = 0
                start = i+1
        return -1 if total<0 else start