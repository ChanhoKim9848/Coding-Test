class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n): 
            for j in range(1+i, n): 
                if nums[i] + nums[j] == target: 
                    return [i,j]

        
        