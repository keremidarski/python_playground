number = int(input('Enter number: '))

counter = 1
sum = 0

while counter <= number:
    if counter % 2 != 0:
        sum += counter
    counter += 1

print(sum)