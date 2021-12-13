number = int(input('Enter number: '))

reminder = 0
sum = 0

while number != 0:
    reminder = number % 10
    sum += reminder
    number = number // 10

print(sum)