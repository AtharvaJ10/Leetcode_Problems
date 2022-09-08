class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {nums1[i]:-1 for i in range(len(nums1))}
        
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]]<nums2[i]:
                if nums2[stack[-1]] in d:
                    d[nums2[stack.pop()]] = nums2[i]
                else:
                    stack.pop()
            stack.append(i)
        return d.values()