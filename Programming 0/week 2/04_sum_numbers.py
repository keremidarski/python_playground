n = int(input('Enter n: '))

counter = 0
numbers = []

while counter < n:
    number = int(input())
    numbers += [number]
    counter += 1

sum = 0

for i in numbers:
    sum += i

print(f'The sum is: {sum}')