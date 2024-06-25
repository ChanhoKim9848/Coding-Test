public class Solution {
    public int MaxSubArray(int[] nums) {
        int s=0;
        int res=nums[0];
        foreach(int i in nums){
            s+=i;
            if (i>s){
                s=i;
            }
            if (res<s){
                res=s;
            }
        }
        return res;
    }
}

/*
The goal is to find the subarray within the given array nums that has the largest sum, and return that sum.
sum is initialized to 0. This variable will keep track of the current subarray sum.
maxSum is initialized to the first element of nums (nums[0]).
A loop iterates through each element of nums using the index i.
each iteration, the current element (nums[i]) is added to sum.

If the current element (nums[i]) is greater than the updated sum, then sum is reset to the value of the current element. 
This step effectively starts a new subarray at the current index
if the current element is greater than the sum accumulated so far.

Updating the maximum subarray sum (maxSum):
If the current sum (which includes the current element) is greater than maxSum, then maxSum is updated to the value of sum. 
This ensures that maxSum always contains the largest sum found during the iterations.
Return the result:

After the loop completes, maxSum contains the largest sum of any subarray within nums,
which is then returned as the result
*/