# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week2/4-Three-More-Problems

number = int(input('Enter number: '))

digit_list = []

while number != 0:
    digit = number % 10
    digit_list = [digit] + digit_list

    number = number // 10

print(f'List of digits is: {digit_list}')

new_number = 0

for i in digit_list:
    new_number = new_number * 10 + i

print(f'Number is: {new_number}')
