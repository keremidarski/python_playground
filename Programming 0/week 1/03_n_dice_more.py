# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week1/1-IO-Simple-Problems

from random import randint

sides = int(input('Enter sides: '))
roll_one = randint(1, sides)
roll_two = randint(1, sides)
roll_three = randint(1, sides)
roll_sum = roll_one + roll_two + roll_three

print(f'First roll: {roll_one}')
print(f'First roll: {roll_two}')
print(f'First roll: {roll_three}')
print(f'Sum is: {roll_sum}')
