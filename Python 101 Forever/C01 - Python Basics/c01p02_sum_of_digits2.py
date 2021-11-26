# Problem description:
# https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/13-C01P02

def sum_of_digits(nums):
    result = 0
    nums = abs(nums)

    while nums > 0:
        digit = nums % 10
        result += digit
        nums = nums // 10

    return result

# Expected: 6
print(sum_of_digits(123))
