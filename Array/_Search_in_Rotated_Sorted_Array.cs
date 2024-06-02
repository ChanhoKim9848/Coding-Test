public class Solution {
    public int Search(int[] nums, int target) {
        int left=0, right=nums.Length-1;

        while(left<=right){
            int mid=(left+right)/2;
            if (nums[mid]==target){
                return mid;
            }
            if (nums[left]<=nums[mid]){
                if (nums[left]<=target && target<nums[mid]){
                    right=mid-1;
                }
                else{
                    left=mid+1;
                }
            }
            else{
                if(nums[mid]<=target && target<=nums[right]){
                    left=mid+1;
                }
                else{
                    right=mid-1;
                }
            }
        }
        return -1;
    }
}


// At any point during the search in the rotated array, 
// one half (either the left or the right) will always be sorted. 
// Determining which half is sorted is crucial for our modified binary search.

// If left half [low...mid][low...mid][low...mid] is sorted: We know this if the element at low\text{low}low is less than or equal to the element at mid\text{mid}mid. In a normally sorted array, if the start is less than or equal to the midpoint, it means all elements till the midpoint are in the correct increasing order.

// If the target lies within this sorted left half: We know this if the target is greater than or equal to the element at low\text{low}low and less than the element at mid\text{mid}mid. If this is the case, we then move our search to this half, meaning, we update high\text{high}high to mid−1\text{mid} - 1mid−1.

// Otherwise: The target must be in the right half. So, we update low\text{low}low to mid+1\text{mid} + 1mid+1.

// If right half [mid...high][mid...high][mid...high] is sorted: This is the else part. If the left half isn't sorted, the right half must be!

// If the target lies within this sorted right half: We know this if the target is greater than the element at mid\text{mid}mid and less than or equal to the element at high\text{high}high. If so, we move our search to this half by updating low\text{low}low to mid+1\text{mid} + 1mid+1.

// Otherwise: The target must be in the left half. So, we update high\text{high}high to mid−1\text{mid} - 1mid−1