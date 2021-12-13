n = int(input('Enter n: '))
start = 0
names = []

while start < n:
    current_name = input()
    names += [current_name]
    start += 1

names.sort()

print('Sorted names are:')
for name in names:
    print(name)