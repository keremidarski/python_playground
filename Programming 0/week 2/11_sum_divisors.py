n = int(input('Enter n: '))

divisors = []

for i in range(1, n):
    if n % i == 0:
        divisors += [i]

sum_divisors = sum(divisors)

print(sum_divisors)