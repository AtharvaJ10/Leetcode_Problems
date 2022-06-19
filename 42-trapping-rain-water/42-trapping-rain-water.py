class Solution:
    def trap(self, height: List[int]) -> int:
        level = []
        max1 = 0
        for i in height:
            max1 = max(max1,i)
            level.append(max(max1,i))
            
        max1=0
        for i in range(len(height)-1,-1,-1):
            max1 = max(max1,height[i])
            level[i] = min(max1,level[i])-height[i]
        return sum(level)
            