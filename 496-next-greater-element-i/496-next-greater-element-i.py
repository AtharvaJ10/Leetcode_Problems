class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = {x:-1 for x in nums1}
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]]<nums2[i]:
                ind = stack.pop()
                if nums2[ind] in greater:
                    greater[nums2[ind]] = nums2[i]
            stack.append(i)
        return greater.values()