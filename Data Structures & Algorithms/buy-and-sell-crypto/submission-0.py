class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for price in prices:
            if min_price > price:
                min_price = price
                continue

            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit
        