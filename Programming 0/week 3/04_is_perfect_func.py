# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week3/2-Resolve-with-Functions

def sum_divisors(n):
    sum = 0

    for i in n:
        sum += i
    return sum

def is_perfect(n):
    divisors = []

    for i in range(1, n):
        if n % i == 0:
            divisors += [i]

    sum = sum_divisors(divisors)

    if sum == n:
        print(f'{n} is a perfect number!')
    else:
        print(f'Sorry! {n} is not a perfect number.')

is_perfect(10)
