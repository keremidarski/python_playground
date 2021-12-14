# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week1/2-If-Elif-Else-Simple-Problems

from random import randint

sides = int(input('Enter dice side: '))
player_one = input('Enter player1 name: ')
player_two = input('Enter player2 name: ')

player_one_roll_one = randint(1, sides)
player_two_roll_one = randint(1, sides)

print(f'{player_one} rolls {player_one_roll_one}')
print(f'{player_two} rolls {player_two_roll_one}')

if player_one_roll_one > player_two_roll_one:
    print(f'{player_one} wins!')
elif player_one_roll_one < player_two_roll_one:
    print(f'{player_two} wins!')
else:
    print("It's a draw!")

