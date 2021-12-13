number_a = int(input('Enter a: '))
number_b = int(input('Enter b: '))

if number_a < number_b:
    while number_a <= number_b:
        print(number_a)
        number_a += 1
elif number_b < number_a:
    while number_b <= number_a:
        print(number_b)
        number_b += 1
else:
    print('The numbers are equal.')