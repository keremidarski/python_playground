# Problem description:
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def max_profit(prices):
    lowest = 0
    highest = 1
    max_p = 0

    while highest < len(prices):
        if prices[lowest] < prices[highest]:
            profit = prices[highest] - prices[lowest]
            max_p = max(max_p, profit)
        else:
            lowest = highest
        
        highest += 1

    return max_p
