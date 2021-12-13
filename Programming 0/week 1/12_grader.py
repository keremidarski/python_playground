points = int(input('Enter points: '))

if points >= 0 and points <= 50:
    print('Слаб 2')
elif points > 50 and points <= 60:
    print('Среден 3')
elif points > 60 and points <= 70:
    print('Добър 4')
elif points > 70 and points <= 80:
    print('Много добър 5')
elif points > 80 and points < 100:
    print('Отличен 6')
elif points == 100:
    print('Невероятен 7')
else:
    print('Invalid points')