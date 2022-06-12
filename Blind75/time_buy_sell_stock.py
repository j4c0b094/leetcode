import math

class Solution:
    """
    PS: You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    """
    # One pass soln. TC : O(n) -- single for loop across list of prices
    def maxProfit(self, prices: List[int]) -> int:      
        mininum_price = math.inf
        max_profit = 0
        for i in range(len(prices)):                
            mininum_price = min(prices[i], mininum_price)
            max_profit = max(max_profit, prices[i] - mininum_price)
        return max_profit