# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week4/5-Coins

def calculate_coins(sum):
    result = {'2lv': 0, '1lv': 0, '50st': 0, '20st': 0, '10st': 0, '5st': 0, '2st': 0, '1st': 0}
    coins = sum * 100

    while coins > 0:
        if coins >= 200:
            result['2lv'] += 1
            coins -= 200
        elif coins >= 100:
            result['1lv'] += 1
            coins -= 100
        elif coins >= 50:
            result['50st'] += 1
            coins -= 50
        elif coins >= 20:
            result['20st'] += 1
            coins -= 20
        elif coins >= 10:
            result['10st'] += 1
            coins -= 10
        elif coins >= 5:
            result['5st'] += 1
            coins -= 5
        elif coins >= 2:
            result['2st'] += 1
            coins -= 2
        elif coins >= 1:
            result['1st'] += 1
            coins -= 1
    return result

print(calculate_coins(8.94))
