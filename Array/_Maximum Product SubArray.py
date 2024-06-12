class Solution(object):
    def maxProduct(self, nums):
        ans=prev_min=prev_max=max_to_n=min_to_n=nums[0]

        for i in nums[1:]:
            min_to_n = min(i,min(prev_min*i,prev_max*i))
            max_to_n = max(i,max(prev_min*i,prev_max*i))

            prev_min = min_to_n
            prev_max = max_to_n
            ans= max(max_to_n,ans)

        return ans
            
            