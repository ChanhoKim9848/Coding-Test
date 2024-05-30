public class Solution {
    public int Search(int[] nums, int target) {
        int idx = 0;
        if (nums[0] > target) {
            idx = nums.Length-1;
            while (idx >= 0 && nums[idx] >= target) {
                if (nums[idx] == target) {
                    return idx;
                }
                idx--;
            }
        } else {
            while (idx < nums.Length && nums[idx] <= target) {
                if (nums[idx] == target) {
                    return idx;
                }
                idx++;
            }
        }
        return -1;
    }
}