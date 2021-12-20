# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week1/5-Saturday-Tasks

n = int(input("Enter a number: "))

start = 1
product = 1

while start <= n:
    product *= start
    start += 1

print(product)
