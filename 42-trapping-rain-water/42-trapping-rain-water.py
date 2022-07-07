class Solution:
    def trap(self, height: List[int]) -> int:
        left, right, lmax, rmax = 0, len(height)-1, 0, 0
        res = 0
        while left<right:
            if height[left]<height[right]:
                if lmax<height[left]:
                    lmax = height[left]
                else:
                    res+= lmax-height[left]
                left+=1
            else:
                if rmax<height[right]:
                    rmax = height[right]
                else:
                    res+=rmax - height[right]
                right-=1
        return res