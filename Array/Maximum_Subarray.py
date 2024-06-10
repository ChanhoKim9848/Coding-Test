class Solution(object):
    def maxSubArray(self, nums):
        s=0
        result=nums[0]
        for i in nums:
            s+=i
            if s<i:
                s=i
            if result<s:
                result=s
        return result
        
        