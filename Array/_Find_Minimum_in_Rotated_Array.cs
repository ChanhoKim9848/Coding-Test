public class Solution {
    public int FindMin(int[] nums) {
        int left=0,right=nums.Length-1;

        while (left<right){
            int mid=(left+right)/2;
            if (nums[mid]<nums[right]){right=mid;}
            else{left=mid+1;}
        }
        return nums[right];
    }
}
/* We start by initializing two pointers: 
   left at the beginning of the array and right at the end of the array.

   The loop continues until left and right converge (i.e., left < right).

   Calculate the midpoint mid of the current left and right indices.
   If the element at mid is less than the element at right, 
   it means the minimum value lies to the left of mid (including mid).
   Thus, we move the right pointer to mid.
   If the element at mid is greater than or equal to the element at right,
   it means the minimum value lies to the right of mid. Thus, we move the left pointer to mid + 1.

   When left and right converge, they point to the minimum element in the array.
   We return the element at the right pointer (or left, since they are the same at this point.

   This algorithm ensures that we find the minimum element in O(log n) time,
   leveraging the properties of the rotated sorted array and binary search.

*/