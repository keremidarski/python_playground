# Problem description:
# https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/13-C01P02

def sum_of_digits(nums):
    result = 0

    for n in str(nums):
        if n == '-':
            continue
        result += int(n)

    return result

# Expected: 1
print(sum_of_digits(-10))
