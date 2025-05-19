# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

from typing import List

class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        
        if n < 2: 
            return 0
        
        max_profit = 0

        current_buy =  prices[0]


        for i in range(1, n):
            
            if prices[i] > current_buy and prices[i] - current_buy > max_profit:
                max_profit = prices[i] - current_buy
            
            elif prices[i] < current_buy:
                current_buy = prices[i]
        

        return max_profit




def __main__():

    A = Solution()

    print("Max profit = {0}, correct = 5".format(A.maxProfit([7,1,5,3,6,4])))
    print("Max profit = {0}, correct = 0".format(A.maxProfit([7,6,4,3,1])))
    print("Max profit = {0}, correct = 10".format(A.maxProfit([7,1,5,3,8,0,10])))


__main__()


####    DEBRIEF     ####
#   Beats 84.6% in time #
#   Beats 8.88% in memory
#########################
