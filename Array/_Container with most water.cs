public class Solution {
    public int MaxArea(int[] height) {
        int max = 0;
        int left=0, right=height.Length-1;

        while (left<right){
            int value = (right-left)*Math.Min(height[left],height[right]);
            if (max<value){
                max=value;
            }

            // when left and right go inward of the array
            // we want to keep the edge height as high as possible
            // so we compare two heights and move the shortest one inward first 
            if(height[left]<=height[right]){
                left++;
            }
            else{
                right--;
            }
        }
    return max;
    }
}

