"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Notice: Must buy before sell it. 

There has three solutions: brute force, dynamic programming, two pointers.
"""

## brute force
def maxProfit(prices):
    arr = []
    
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if (prices[j] - prices[i]) > 0:
                arr.append(prices[j] - prices[i])
    
    if arr:
        return max(arr)
    else:
        return 0


## Dynamic programming 
def maxProfit_2(prices):
    maxprofit = 0
    minprice = prices[0] ## The price what you buy is minimal.
    
    for i in range(1, len(prices)):
        if prices[i] < minprice: ## If the current prices what you bought is minimal ??
            minprice = prices[i]
        if (prices[i] - minprice) > maxprofit: ## Maximize the profit. 
            maxprofit = prices[i] - minprice
    
    return maxprofit


## Two pointers. 
def maxProfit_3(prices):
    l, r = 0, 1 ## define two pointers, left and right
    maxprofit = 0
    
    while r < len(prices):
        ## profitable ??
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxprofit = max(maxprofit, profit)
            r += 1
        else:
            l = r
            r += 1
    
    return maxprofit
                