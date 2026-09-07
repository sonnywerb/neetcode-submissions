class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dynamic programming solution
        min_buy = prices[0]
        max_profit = 0

        for sell in prices:
            max_profit = max(max_profit, sell - min_buy)
            min_buy = min(min_buy, sell)
        
        return max_profit