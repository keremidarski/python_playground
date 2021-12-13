n = int(input('Enter n: '))

start = 0
numbers = []

while start < n:
    number = int(input())
    numbers += [number]
    start += 1

avg = sum(numbers) / len(numbers)
print(f'Avg is {avg:.2f}')