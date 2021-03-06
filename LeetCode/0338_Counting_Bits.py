# Problem description:
# https://leetcode.com/problems/counting-bits/

def count_bits(n):
    dp = [0] * (n + 1)
    offset = 1

    for i in range(1, n + 1):
        if offset * 2 == i:
            offset = i
        
        dp[i] = 1 + dp[i - offset]

    return dp


# Expected: [0, 1, 1]
print(count_bits(2))
# Expected: [0, 1, 1, 2, 1, 2]
print(count_bits(5))
