class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        z=0
        for i in range(len(nums)):
            if nums[i]:
                nums[i],nums[z]=nums[z],nums[i]
                z+=1