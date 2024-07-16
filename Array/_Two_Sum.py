class Solution(object):
    def twoSum(self, nums, target):

        # create an empty hash table to store elements and their indices
        # iterate through the array from left to right
        # for each element of nums[i], calculate the complement by 
        # subtracting it from the target
        # check if the complement exists in the hash table,
        # we found a solution if it has
        # if no solution found then return empty array
        hash={}
        n=len(nums)
        for i in range(n):
            hash[nums[i]]=i
        
        for i in range(n):
            complement = target -nums[i]
            if hash[complement] and hash[complement]!=i:
                return [i,hash[complement]]
        return []
    



    def twoSum(self, nums, target):
        h={}
        for index,number in enumerate(nums):
            dif=target-number
            if dif in h:
                return [h[dif],index]
            h[number]=index
        return




        