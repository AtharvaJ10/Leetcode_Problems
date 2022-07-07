class Solution:
    def trap(self, height: List[int]) -> int:
        array = []
        res = 0
        max1 = 0
        for i in height:
            max1 = max(i, max1)
            array.append(max1)
        
        max1 = 0
        for i in range(len(height)-1,-1,-1):
            max1 = max(height[i], max1)
            array[i] = min(max1, array[i]) - height[i]
        return sum(array)