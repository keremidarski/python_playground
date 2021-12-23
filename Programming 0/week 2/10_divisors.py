# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week2/3-Simple-Algorithms

n = int(input('Enter n: '))

divisors = []

for i in range(1, n):
    if n % i == 0:
        divisors += [i]

print(divisors)
