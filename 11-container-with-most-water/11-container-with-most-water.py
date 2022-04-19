class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0,len(height)-1
        result = 0
        while i<j:
            if height[j]>height[i]:
                if result < height[i]*(j-i):
                    result = height[i]*(j-i)
                i+=1
            else:
                if result < height[j]*(j-i):
                    result = height[j]*(j-i)
                j-=1
        return result