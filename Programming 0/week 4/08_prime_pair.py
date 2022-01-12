# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week4/8-Pair-With-Prime-Sum

def is_prime(n):
    start = 2
    is_prime = True
    
    if n > 2:
        while start < n:
            if n % start == 0:
                is_prime = False
                break

            start += 1
    else:
        is_prime = False

    return is_prime


def count_zero_pairs(numbers):
    count = 0
    prime = False
    n = len(numbers)
    
    for x_index in range(0, n):
        for y_index in range(x_index, n):
            x = numbers[x_index]
            y = numbers[y_index]

            prime_number = x + y

            if is_prime(prime_number):
                count += 1

    if count != 0:
        prime = True
        
    return prime


print(count_zero_pairs([5, 2]))
