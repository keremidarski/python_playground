number = int(input('Enter number: '))

primes = 0

while number != 0:
    digit = number % 10
    counter = 0

    for i in range(1, digit + 1):
        if digit % i == 0:
            counter += 1

    if counter == 2:
        primes += 1

    number = number // 10

if primes == 0:
    print('No')
else:
    print('Yes')