class Solution(object):
    def maxProfit(self, prices):
        profit=0
        min_price = prices[0]
        for i in range(1,len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            if profit< prices[i]-min_price:
                profit=prices[i]-min_price
        return profit


            
        

        