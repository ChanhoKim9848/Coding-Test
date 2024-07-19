class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res= []
        nums.sort()
        for i,a in enumerate(nums):
            # since we do not want to use the same value twice
            # i>0 means it is not the first value
            if i>0 and a == nums[i-1]:
                continue
            
            # if it is not, we use two pointer this time
            # l is the next value, l is end of the array value
            l, r = i+1, len(nums)-1

            while l<r:
                threeSum = a + nums[l] + nums[r]
                # if threeSum >0
                # we decrement r by 1, shift to the left
                if threeSum > 0 :
                    r-=1
                # otherwise, l increments by 1, shift to the right
                # we could this because the array is sorted in ascending order
                elif threeSum < 0 :
                    l+=1
                else:
                    # we add the result
                    res.append([a,nums[l],nums[r]])
                    # what if we have this kind of array
                    # [-2, -2, 0, 0, 2, 2]
                    #  l                r  this case 
                    # then we want to update l + 1 as l=-2
                    # [-2, -2, 0, 0, 2, 2]
                    #       l           r
                    # but it is again -2, this case we want to update
                    # one more time to get over here
                    # [-2, -2, 0, 0, 2, 2]
                    #          l        r
                    # and that case, now threeSum >0 
                    # loop will execute r-1, right
                    # but we notice that right value now is same as previous one
                    # it is fine because our sum will evaluate sum and shift r again
                    # therefore, each value will only have one corresponding value
                    # that it can sum equal to 0
                    # so we only update l, we don't want to have the same sum
                    # we need to use loop above
                    l+=1
                    
                    # if left value now and the previous one is same
                    # and make sure l<r then we increment l again
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
            return res


                    