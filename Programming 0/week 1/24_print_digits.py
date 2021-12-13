number = int(input('Enter number: '))

reminder = 0

while number != 0:
    reminder = number % 10
    print(reminder)
    number = number // 10