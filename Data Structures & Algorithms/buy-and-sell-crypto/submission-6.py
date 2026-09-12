class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy, max_p = prices[0], 0

        for i in range(1, len(prices)):
            min_buy = min(min_buy, prices[i - 1])

            max_p = max(max_p, prices[i] - min_buy)
            
        return max_p

        