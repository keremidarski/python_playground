# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week3/2-Resolve-with-Functions

def divisors(n):
    divisors = []

    for i in range(1, n):
        if n % i == 0:
            divisors += [i]
            
    return divisors

def sum_divisors(n):
    sum = 0

    for i in n:
        sum += i
        
    return sum

func1 = divisors(10)
func2 = sum_divisors(func1)

print(func2)
