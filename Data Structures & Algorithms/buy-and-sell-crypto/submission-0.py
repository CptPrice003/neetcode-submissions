class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        min = prices[0]
        i = 1

        while i < len(prices):

            if prices[i] < min:

                min = prices[i]

            if prices[i] > min:

                max_profit = max(max_profit, prices[i] - min)

            i += 1

        return max_profit
        