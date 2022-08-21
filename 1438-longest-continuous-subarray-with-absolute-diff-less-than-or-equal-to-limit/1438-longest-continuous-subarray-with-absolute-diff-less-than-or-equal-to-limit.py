from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxd = deque([])
        mind = deque([])
        i = 0
        for j in range(len(nums)):
            while maxd and nums[maxd[-1]]<nums[j]:
                maxd.pop()
            maxd.append(j)
            
            while mind and nums[mind[-1]]>nums[j]:
                mind.pop()
            mind.append(j)
            
            if nums[maxd[0]]-nums[mind[0]]>limit:
                if nums[maxd[0]]==nums[i]:
                    maxd.popleft()
                if nums[mind[0]]==nums[i]:
                    mind.popleft()
                i+=1
        return len(nums)-i