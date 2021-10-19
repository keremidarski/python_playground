# https://leetcode.com/problems/reverse-integer/

# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

def reverse_integer(x):
    result = 0

    if x < 0:
        symbol = -1
        x = -x
    else:
        symbol = 1

    while x:
        result = result * 10 + x % 10
        x //= 10

    return 0 if result > pow(2, 31) else result * symbol

# Expected: 21
print(reverse_integer(120))
