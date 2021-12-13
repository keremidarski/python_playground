n = int(input('Enter n: '))

counter = 0
evens_count = 0
evens = []

while counter < n:
    number = int(input())
    
    if number % 2 == 0:
        evens_count += 1
        evens += [number]
    counter += 1

print(f'Count of evens: {evens_count}')
print('Evens are:')
for i in evens:
    print(i)