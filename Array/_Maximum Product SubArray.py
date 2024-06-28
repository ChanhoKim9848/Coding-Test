class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curMax=curMin=1
        for n in nums:
            if n==0:
                curMin=curMax=1
                continue
            tmp=curMax*n
            curMax=max(n, n*curMax, n*curMin)
            curMin=min(n, n*curMin, tmp)
            res=max(res, curMax)
        return res

