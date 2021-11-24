def fact(n):
    start = 1
    product = 1

    while start <= n:
        product *= start
        start += 1
    return product

def num_to_digit(nums):
    result = []

    for n in str(nums):
        result.append(int(n))
    return result

def fact_digits(n):
    n = abs(n)
    result = 0
    num_list = num_to_digit(n)
    
    for num in num_list:
        num_fact = fact(num)
        result += num_fact
    return result

print(fact_digits(145))