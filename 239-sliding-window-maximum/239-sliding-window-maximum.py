from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque([])
        for i in range(k):
            while queue and nums[queue[-1]]<nums[i]:
                queue.pop()
            queue.append(i)
        
        res = []
        res.append(nums[queue[0]])

        for i in range(k, len(nums)):
            if queue[0]<i-k+1:
                queue.popleft()
            
            while queue and nums[queue[-1]]<nums[i]:
                queue.pop()
            queue.append(i)
            
            res.append(nums[queue[0]])
            
        return res