class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        for i in range(len(prices)):
            sell = prices[i]
            for j in range(0, i):
                if prices[j] < sell:
                    profit = sell - prices[j]
                    if profit > best_profit:
                        best_profit = profit
        
        return best_profit