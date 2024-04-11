class Solution(object):
    def minOperations(self, nums):
        res=0
        for i in range(len(nums)-1):
            if nums[i]>=nums[i+1]:
                res+=nums[i]-nums[i+1] + 1
                nums[i+1] += nums[i]-nums[i+1] + 1
        return res
print(Solution.minOperations(Solution,[1,1,1]))
