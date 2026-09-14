class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0

        l, r = 0, 1

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r

            profit = prices[r] - prices[l]
            max_p = max(max_p, profit)
            r += 1
        
        return max_p

            