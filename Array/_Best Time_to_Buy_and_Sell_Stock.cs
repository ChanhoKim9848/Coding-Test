public class Solution {
    // we iterate through prices array, time complexity is then O(N)
    // for space complexity, we only use variable takes constant time
    // we initialize min to store the minimum price
    // and we store the maximum difference between min and max prices
    // if the dif is higher than before, then we keep update dif
    // finally we can find the maximum dif and return it
    public int MaxProfit(int[] prices) {
        int dif = 0;
        int min = prices[0];
        for (int i=1; i<prices.Length; i++){
            if (prices[i]<min){
                min=prices[i];
            }
            else if (prices[i]-min>dif){
                dif=prices[i]-min;
            }
        }
        return dif;
    }
}