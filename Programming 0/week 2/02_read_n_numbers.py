n = int(input("Enter count of numbers: "))

count = 1
numbers = []

while count <= n:
    number = int(input("Enter number: "))
    numbers = numbers + [number]
    count += 1

print(numbers)