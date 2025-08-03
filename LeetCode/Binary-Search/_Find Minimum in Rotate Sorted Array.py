class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # if this is right, we are in sorted array
            # get the minimum, left is obviously left and break loop
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            # if not in sorted array
            # find middle,
            m = (l + r) // 2
            res = min(res, nums[m])
            # if middle is all the way left is greater, 
            # then m is definitely in left sorted array
            if nums[m] >= nums[l]:
            # as we rotate, left sorted array is always greater than right sorted array
                l = m + 1
            else:
                r = m - 1
        return res
    
    # when search for the middle 