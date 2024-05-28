public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int[] a = new int[nums.Length];
        int n = 0;
        int s = 1;
        foreach(int e in nums){
            if (e==0){
                n+=1;
            }
            else{
                s*=e;
            }
        }
        for(int i=0;i<nums.Length;i++){
            if (nums[i]!=0){
                if(n>0){
                    a[i]=0;
                }
                else{
                    a[i]=s/nums[i];
                }
            }
            else if(n>1){
                a[i]=0;
                }
            else{
                a[i]=s;
            }
         }
            return a;
    }
}
        
