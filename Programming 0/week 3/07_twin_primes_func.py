def is_prime(n):
    start = 2
    is_prime = True

    while start < n:
        if n % start == 0:
            is_prime = False
            break

        start += 1

    return is_prime

def twin_prime(p):

    if is_prime(p) == False:
        print(f'{p} is not a prime.')
    else:
        q = p + 2
        z = p - 2

        if is_prime(q) == True or is_prime(z) == True:
            print(f'Twin primes with {p}:')
            if is_prime(z) == True:
                print(f'{z}, {p}')
            if is_prime(q) == True:
                print(f'{p}, {q}')
        else:
            print(f'{p} is prime but:')
            print(f'{z} is not')
            print(f'{q} is not')

twin_prime(23)