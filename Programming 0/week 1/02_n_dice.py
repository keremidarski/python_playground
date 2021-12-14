# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week1/1-IO-Simple-Problems

from random import randint

sides = int(input('Enter sides: '))
dice = randint(1, sides)

print(f'The dice rolled: {dice}')
