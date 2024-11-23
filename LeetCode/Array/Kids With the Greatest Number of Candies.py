class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        M=max(candies)
        return [candy + extraCandies >=M for candy in candies]