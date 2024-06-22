class Solution(object):
    def maxSubArray(self, nums):
        current=nums[0]
        res=nums[0]
        for i in range(1,len(nums)):
            current=max(nums[i],nums[i]+current)
            res=max(res,current)
        return res
    
print(Solution.maxSubArray(Solution,[-2,1,-3,4,-1,2,1,-5,4]))