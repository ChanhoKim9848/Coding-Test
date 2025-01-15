class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        maxRight = [0] * n  # maxRight[i] is the maximum element among nums[i+1...n-1]
        maxRight[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            maxRight[i] = max(maxRight[i+1], nums[i+1])
            
        minLeft = nums[0]
        for i in range(1, n-1):
            if minLeft < nums[i] < maxRight[i]:
                return True
            minLeft = min(minLeft, nums[i])
        return False

# Time: O(N), where N <= 5*10^5 is length of nums array.
# Space: O(N)

# first=second=math.inf
#         for n in nums:
#             if n<=first:
#                 first=n
#             elif n<=second:
#                 second=n
#             else:
#                 return True
#         return False