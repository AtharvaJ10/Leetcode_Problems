class Solution:
    def trap(self, height: List[int]) -> int:
        left,right = 0,len(height)-1
        maxl,maxr = 0,0
        res = 0
        
        while left<right:
            if height[left]<height[right]:
                if maxl<height[left]:
                    maxl=height[left]
                else:
                    res+=maxl-height[left]
                left+=1
            else:
                if maxr<height[right]:
                    maxr=height[right]
                else:
                    res+=maxr-height[right]
                right-=1
                
        return res
            
                