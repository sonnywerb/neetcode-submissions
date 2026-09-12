class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l, r = 0, 1
        max_p = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                max_p = max(max_p, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return max_p
        # DP/greedy algorithm
        # min_buy, max_p = prices[0], 0

        # for i in range(len(prices)):
        #     min_buy = min(min_buy, prices[i])
        #     max_p = max(max_p, prices[i] - min_buy)
            
        # return max_p

        