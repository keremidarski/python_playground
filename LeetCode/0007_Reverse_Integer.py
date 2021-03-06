# Problem description:
# https://leetcode.com/problems/reverse-integer/

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
