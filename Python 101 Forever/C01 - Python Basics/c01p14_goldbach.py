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

def goldbach(n):
    result = []
    p = 2

    if n % 2 == 1 or n <= 2:
        return None

    while p < n:
        p2 = n - p
        if is_prime(p2) and (p2, p) not in result:
            result.append((p, p2))
            p = next_prime(p)
        else:
            p = next_prime(p)
    return result

print(goldbach(5))