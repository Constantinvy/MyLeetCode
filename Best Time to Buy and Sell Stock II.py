#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/?envType=study-plan-v2&envId=top-interview-150

"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
"""

from typing import List

class Solution:

    size = 0
    memory = {}


    def maxProfit(self, prices):

        self.memory = {}
        self.size = len(prices)

        return self.maxProfitBought(prices)
    

    def maxProfitBought(self, prices: List[int]) -> int:
        
        if (len(prices)<=1):
            return 0
        
        if self.size - len(prices) in self.memory:
            return self.memory[self.size - len(prices)]

        a = self.maxProfitSell(prices[1:], prices[0])
        b = self.maxProfitBought(prices[1:])

        self.memory[self.size - len(prices)] = max(a,b)

        return max(a,b)
    
    
    def maxProfitSell(self, prices, bought_price):

        if len(prices) == 1:
            return max(0, prices[0] - bought_price)


        if len(prices) == 0:
            return 0

   
        return max(prices[0] - bought_price + self.maxProfitBought(prices[1:]), self.maxProfitSell(prices[1:], bought_price))







def __main__():

    A = Solution()

    print("Max profit = {0}, correct = 0".format(A.maxProfit([7,1])))
    print("Max profit = {0}, correct = 7".format(A.maxProfit([7,1,5,3,6,4])))
    print("Max profit = {0}, correct = 0".format(A.maxProfit([7,6,4,3,1])))
    print("Max profit = {0}, correct = 4".format(A.maxProfit([1,2,3,4,5])))


__main__()



####       DEBRIEF      ####
#       MEMORY EXCEEDED
# => WRONG APPROACH !!!! Should simply compute all the positive sum between consequitive days !!!
