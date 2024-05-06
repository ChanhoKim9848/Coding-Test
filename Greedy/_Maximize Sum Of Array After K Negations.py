class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        nums.sort()
        i=0
        while i<len(nums) and nums[i]<0 and i<k:
            nums[i]=-nums[i]
            i+=1
        return sum(nums)-(k-i)%2 * min(nums)*2
    
#  Sorting: We begin by sorting the array nums in ascending order.
#  This step ensures that the negative numbers,
#  which we intend to manipulate to maximize the sum, are positioned at the start of the array.
#  Iterative Negation: We iterate through the sorted array, 
#  focusing solely on its negative elements.
#  During this iteration, we ensure two conditions: (a) the index i remains within the bounds of the array's length,
#  and (b) the count of negations (i) doesn't exceed the prescribed limit k.
#  Adjusting Sum: Once we've completed the iteration through negative elements,
#  we sum up all elements in the array. However, to optimize this sum for maximum value,
#  we subtract the minimum element in the array.
#  This step is crucial as it converts the minimum element to its negative counterpart,
#  contributing to the overall sum.
#  Handling Odd K: Additionally, we account for the scenario where k is an odd number.
#  In such cases, to balance the negations and
#  maintain the maximum sum, we negate the minimum element once more.
#  This adjustment is necessary to ensure that every negation contributes to the overall sum optimally.

# Time complexity: O(n log n)
# Space complexity: O(n) if using an in-place sorting algorithm;
# otherwise, O(1) for sorting and O(n) for the input array.