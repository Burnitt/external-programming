class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0 
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                prof = price - min_price
                if prof > max_profit:
                    max_profit = prof
        return max_profit
        
