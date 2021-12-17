# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week1/5-Saturday-Tasks

number = int(input('Enter number: '))

reminder = 0

while number != 0:
    reminder = number % 10
    print(reminder)
    number = number // 10
