# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week1/5-Saturday-Tasks

number = int(input('Enter number: '))

counter = 0

for i in range(2, number + 1):
    if number % i == 0:
        counter += 1

if counter == 1:
    print('The number is prime!')
else:
    print('The number is not prime.')
