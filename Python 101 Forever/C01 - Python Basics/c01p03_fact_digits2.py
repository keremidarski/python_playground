# Problem description:
# https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/14-C01P03

def fact(n):
    result = 1

    for x in range(1, n + 1):
        result *= x

    return result

def fact_digits(n):
    result = 0
    n = abs(n)

    while n > 0:
        digit = n % 10
        result += fact(digit)
        n = n // 10

    return result

# Expected: 145
print(fact_digits(145))
