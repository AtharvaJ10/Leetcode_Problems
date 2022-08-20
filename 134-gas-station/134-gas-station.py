class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        total = 0
        current = 0
        for i in range(len(gas)):
            current+=gas[i]-cost[i]
            total+=gas[i]-cost[i]
            if current<0:
                start = i+1
                current = 0
        return start if total>=0 else -1