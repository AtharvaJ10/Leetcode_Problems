class Solution:
    def trap(self, height: List[int]) -> int:
        left,right = 0,len(height)-1
        maxl,maxr = 0,0
        res = 0
        
        while left<right:
            if height[left]>maxl:
                maxl = height[left]
            else:
                res+=maxl-height[left]
            
            if height[right]>maxr:
                maxr = height[right]
            else:
                res+=maxr-height[right]
                
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return res
            
                