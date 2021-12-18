# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week1/5-Saturday-Tasks

number = int(input('Enter number: '))

reversed_number = 0

while number != 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit

    number = number // 10

print(f'The reversed number is: {reversed_number}')
