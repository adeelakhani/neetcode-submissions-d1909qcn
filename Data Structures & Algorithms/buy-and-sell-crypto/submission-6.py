class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        minPrice = prices[0]
        maxProfit = 0
        for price in prices:
            if price <= minPrice:
                minPrice = price
            else:
                profit = price - minPrice
                if profit > maxProfit:
                    maxProfit = profit
        return maxProfit


        