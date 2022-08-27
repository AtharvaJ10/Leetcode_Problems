from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxd = deque([])
        mind = deque([])
        j = 0
        for i in range(len(nums)):
            while maxd and nums[maxd[-1]]<nums[i]:
                maxd.pop()
            maxd.append(i)
            
            while mind and nums[mind[-1]]>nums[i]:
                mind.pop()
            mind.append(i)
            
            if nums[maxd[0]]-nums[mind[0]]>limit:
                if nums[maxd[0]]==nums[j]:
                    maxd.popleft()
                if nums[mind[0]]==nums[j]:
                    mind.popleft()
                j+=1
        return len(nums)-j