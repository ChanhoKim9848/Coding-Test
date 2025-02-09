class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        res= []
        for i, a in enumerate(nums):
            if a>0:
                break
            if i>0 and nums[i]==nums[i-1]:  # if it is not first element and not same as prev one
                continue

            l,r = i+1,n-1
            # initialize left and right
            while l<r:

                threeSum = a + nums[l] + nums[r]

                if threeSum > 0 :
                    r-=1
                elif threeSum <0 :
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    r-=1
                    l+=1
                    # increment left pointer till the prev one is not same
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        return res
                