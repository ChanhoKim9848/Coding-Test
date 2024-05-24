public class Solution {

    /*
Create a List: Start with a list of integers called nums.
Convert to a Set: Convert this list to a HashSet<int>. A HashSet in C# automatically removes duplicate elements, 
so any duplicates in the list will be eliminated when it's converted to a set.
Compare Lengths: Compare the count of elements in the original list (nums.Count) with the count of elements in the HashSet (uniqueNums.Count).
If the counts are the same, it means there were no duplicates in the original list.
If the counts are different, it means there were duplicates in the original list.
    */
    public bool ContainsDuplicate(int[] nums) {
        HashSet<int> set = new HashSet<int>(nums);
        return nums.Length != set.Count;
    }
}