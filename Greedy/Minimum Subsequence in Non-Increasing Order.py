class Solution(object):
    def minSubsequence(self, nums):
        res=[]
        nums.sort()
        s=sum(nums)

        for i in range(len(nums)-1,-1,-1):
            if sum(res)<=s:
                s-=nums[i]
                res.append(nums[i])
        return res

print(Solution.minSubsequence(Solution,[4,3,10,9,8]))