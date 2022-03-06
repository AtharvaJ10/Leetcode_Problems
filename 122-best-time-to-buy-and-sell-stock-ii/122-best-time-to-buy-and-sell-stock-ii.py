class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        
        profit,buy = 0,prices[0]
        for i in range(1,len(prices)):
            if prices[i]-buy<=0:
                buy = prices[i]
            elif prices[i]-buy>0:
                profit+=prices[i]-buy
                buy = prices[i]
        return profit