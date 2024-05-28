class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        return sum(sorted(nums)[::2])


print(Solution.arrayPairSum(Solution,[3,1,2,2,5,6]))