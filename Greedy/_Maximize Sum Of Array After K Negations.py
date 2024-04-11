class Solution(object):
    def largestSumAfterKNegations(self, nums, k):

        nums.sort()
        
        i=0
        while i<len(nums) and nums[i]<0 and i<k:
            nums[i]=-nums[i]
            i+=1
        return sum(nums)-(k-i)%2 * min(nums)*2