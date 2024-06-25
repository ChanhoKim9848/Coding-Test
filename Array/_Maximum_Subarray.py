class Solution(object):
    def maxSubArray(self, nums):
        s=0
        res=nums[0]
        for i in nums:
            s+=i
            if s<i:
                s=i
            if res<s:
                res=s
        return res

    
print(Solution.maxSubArray(Solution,[-2,1,-3,4,-1,2,1,-5,4]))