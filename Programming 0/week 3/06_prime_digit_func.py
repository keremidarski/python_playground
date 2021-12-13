def is_prime(n):
    start = 2
    is_prime = True

    while start < n:
        if n % start == 0:
            is_prime = False
            break

        start += 1

    return is_prime

def to_digits(n):
    primes = 0
    are_primes = True

    while n != 0:
        digit = n % 10

        if is_prime(digit):
            primes += 1
        
        n = n // 10

        if primes == 0:
            are_primes = False

    return are_primes

print(to_digits(867))