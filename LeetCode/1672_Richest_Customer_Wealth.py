# https://leetcode.com/problems/richest-customer-wealth/

# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i-th customer has in the j-th bank.
# Return the wealth that the richest customer has. A customer's wealth is the amount of money they have in all their bank accounts. 
# The richest customer is the customer that has the maximum wealth.

def maximum_wealth(accounts):
    max_wealth = 0
    
    for account in accounts:
        if sum(account) > max_wealth:
            max_wealth = sum(account)

    return max_wealth

# Expected: 17
print(maximum_wealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))
