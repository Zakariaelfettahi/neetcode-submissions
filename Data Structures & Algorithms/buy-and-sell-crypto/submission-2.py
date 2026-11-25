class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) ==1:
            return 0
        
        max_profit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - min(prices[:i])
            max_profit = max(max_profit, profit)

        return max_profit
            