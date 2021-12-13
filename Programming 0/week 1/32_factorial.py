n = int(input("Enter a number: "))

start = 1
product = 1

while start <= n:
    product *= start
    start += 1

print(product)