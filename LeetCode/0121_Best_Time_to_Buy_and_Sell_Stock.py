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


# Expected: 5
print(max_profit([7, 1, 5, 3, 6, 4]))
# Expected: 0
print(max_profit([7, 6, 4, 3, 1]))
