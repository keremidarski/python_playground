number_a = int(input('Enter a: '))
number_b = int(input('Enter b: '))

if number_a < number_b:
    while number_a <= number_b:
        if number_a % 2 == 0:
            print(f'{number_a} - even')
        else:
            print(f'{number_a} - odd')
        number_a += 1
elif number_b < number_a:
    while number_b <= number_a:
        if number_b % 2 == 0:
            print(f'{number_b} - even')
        else:
            print(f'{number_b} - odd')
        number_b += 1
else:
    print('The numbers are equal.')