def divisors(n):
    divisors = []

    for i in range(1, n):
        if n % i == 0:
            divisors += [i]
    return divisors

print(divisors(10))