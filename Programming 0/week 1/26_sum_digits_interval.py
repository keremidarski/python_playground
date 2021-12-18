# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week1/5-Saturday-Tasks

num_n = int(input('Enter N: '))
num_m = int(input('Enter M: '))

number = num_n

while number <= num_m:
    current_number = number
    reminder = 0
    sum = 0
    while current_number != 0:
        reminder = current_number % 10
        sum += reminder
        current_number = current_number // 10
    print(f'Sum of digits of {number} = {sum}')
    number += 1
