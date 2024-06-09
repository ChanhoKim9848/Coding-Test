class Solution(object):
    def containsDuplicate(self, nums):
        return len(set(nums))!=len(nums)

print(Solution.containsDuplicate(Solution,[1,2,3,1]))