def maximum_wealth(accounts):
    max_wealth = 0
    
    for account in accounts:
        if sum(account) > max_wealth:
            max_wealth = sum(account)

    return max_wealth

print(maximum_wealth([[2,8,7],[7,1,3],[1,9,5]]))