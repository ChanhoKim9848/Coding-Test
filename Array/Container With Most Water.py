class Solution(object):
    def maxArea(self, height):
        left,right=0,len(height)-1
        res=0
        while left<right:
            a=min(height[left],height[right])*(right-left)
            if a>res:res=a
            if height[left]<height[right]:
                left+=1
            else:right-=1
        return res