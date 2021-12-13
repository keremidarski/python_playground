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
        return sum
    else:
        pass

def first_n_perfect(n):
    start = 6

    while True:
        if is_perfect(start) != None:
            print(is_perfect(start))
            n -= 1
        
        if n == 0:
            break
        
        start += 1

first_n_perfect(3)