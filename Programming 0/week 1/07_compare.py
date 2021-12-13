num_a = int(input('Enter a: '))
num_b = int(input('Enter b: '))

if num_a > num_b:
    print(f'a({num_a}) is bigger than b({num_b})!')
elif num_a < num_b:
    print(f'b({num_b}) is bigger than a({num_a})!')
else:
    print(f'a({num_a}) is equal to b({num_b})!')