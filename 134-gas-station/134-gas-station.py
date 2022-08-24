class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr, total = 0,0
        start = 0
        for i in range(len(gas)):
            curr+=gas[i]-cost[i]
            total+=gas[i]-cost[i]
            if curr<0:
                start = i+1
                curr = 0
        return start if total>=0 else -1