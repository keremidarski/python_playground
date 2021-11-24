from itertools import combinations_with_replacement

def is_prime(n):
    if n < 2:
        return False

    for d in range(2, n):
        if n % d == 0:
            return False
    return True

def goldbach(n):
    if n <= 2 or n % 2 == 1:
        return

    result = []
    primes = [x for x in range(2, n) if is_prime(x)]

    for p1, p2 in combinations_with_replacement(primes, 2):
        if p1 + p2 == n:
            result.append((p1, p2))
    return result

print(goldbach(10))