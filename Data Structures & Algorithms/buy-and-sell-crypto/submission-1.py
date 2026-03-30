class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        l, r = 0, 1
        i: int = 0
        profit: int = 0
        while r <= (len(prices)-1):
            if prices[r] < prices[l]:
                l = r
                r+=1
            if (prices[r] - prices[l]) > profit:
                profit = prices[r] - prices[l]
        return profit
            