class Solution(object):
    def twoSum(self, nums, target):
        h={}
        for index,number in enumerate(nums):
            dif=target-number
            if dif in h:
                return [h[dif],index]
            h[number]=index
        return




        