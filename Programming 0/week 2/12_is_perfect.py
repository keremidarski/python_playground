n = int(input('Enter n: '))

divisors = []

for i in range(1, n):
    if n % i == 0:
        divisors += [i]

sum_divisors = sum(divisors)

if sum_divisors == n:
    print(f'{n} is a perfect number!')
else:
    print(f'Sorry! {n} is not a perfect number.')