from random import randint

maria_score = 1001
ivan_score = 1001

while maria_score != 0 or ivan_score != 0:
    if maria_score == 0:
        print('Maria wins!')
        break
    if ivan_score == 0:
        print('Ivan wins!')
        break

    if maria_score > 0:
        maria_roll = randint(1, 30)
        maria_score -= maria_roll
        print(f'Maria rolled {maria_roll}! Her current score is {maria_score}.')
    else:
        maria_roll = randint(1, 30)
        maria_score += maria_roll
        print(f'Maria rolled {maria_roll}! Her current score is {maria_score}.')
    
    if ivan_score > 0:
        ivan_roll = randint(1, 30)
        ivan_score -= ivan_roll
        print(f'Ivan rolled {ivan_roll}! His current score is {ivan_score}.')
    else:
        ivan_roll = randint(1, 30)
        ivan_score += ivan_roll
        print(f'Ivan rolled {ivan_roll}! His current score is {ivan_score}.')