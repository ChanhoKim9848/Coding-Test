class Solution(object):
    def maximizeSum(self, nums, k):
        return max(nums) * k + (k * (k - 1)) / 2
    
#     We find max element m, and the result is m + (m + 1) ... + (m + k - 1).

# We can rewrite this as k * m plus 0 + 1 + 2 + ... k - 1.

# We compute the second part using the formula for the sum of arithmetic progression: k * (k - 1) / 2.