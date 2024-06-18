class Solution(object):
    def maxProfit(self, prices):
        minimum=prices[0]
        res=0
        for i in range(1,len(prices)):
            if minimum>prices[i]:
                minimum=prices[i]
            elif res<prices[i]-minimum:
                res=prices[i]-minimum
        return res

        



        