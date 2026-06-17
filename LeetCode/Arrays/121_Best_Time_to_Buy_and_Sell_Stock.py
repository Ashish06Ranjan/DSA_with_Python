"""

Problem : 121. Best Time to Buy and Sell Stock
Approach : Store the minimum stock price seen so far. For each day, calculate the profit if sold on that day.
            Update the maximum profit whenever a larger profit is found.
            Return the maximum profit
            
"""

class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for i in prices:
            if i < min_price:
                min_price = i

            profit = i - min_price

            if profit > max_profit:
                max_profit = profit
        return max_profit
