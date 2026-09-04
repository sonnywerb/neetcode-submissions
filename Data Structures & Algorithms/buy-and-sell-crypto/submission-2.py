class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        l, r = 0, 1
        while l < len(prices):
            profit = 0
            if r < len(prices) and prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
                r += 1
            else:
                l = r
                r += 1
        return max_profit
            

        
        # [10,1,5,6,7,1]