class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        res=0
        while i<j:
            amount = (j-i) * min(height[i],height[j])
            res = max(amount,res)
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
        return res