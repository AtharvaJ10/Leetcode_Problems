class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit,buy = 0,prices[0]
        if len(prices)==1:
            return profit
        for i in range(1,len(prices)):
            if prices[i]-buy<0:
                buy = prices[i]
            elif prices[i]-buy>profit:
                profit = prices[i]-buy
        return profit
        