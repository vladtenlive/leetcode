class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
          price = prices[i]
          max_profit = max(price - min_price, max_profit)
          min_price = min(price, min_price)

        return max_profit