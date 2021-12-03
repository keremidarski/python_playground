# Problem description:
# https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/24-C01P13

def is_prime(n):
    counter = 0

    for i in range(1, n + 1):
        if n % i == 0:
            counter += 1
            
    return counter == 2


def next_prime(n):
    n += 1

    while not is_prime(n):
        n += 1
        
    return n


def prime_factorization(n):
    result = []
    
    p = 2
    a = 0

    while n != 1:
        while n % p == 0:
            a += 1
            n = n // p

        if a > 0:
            result.append((p, a))

        a = 0
        p = next_prime(p)

    return result

# Expected: [(2, 1), (5, 1)]
print(prime_factorization(10))
