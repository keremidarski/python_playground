# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week1/5-Saturday-Tasks

num_n = int(input('Enter N: '))
num_m = int(input('Enter M: '))

if num_n % 10 == num_m % 10:
    if num_n > num_m:
        print(num_n)
    elif num_n < num_m:
        print(num_m)
    else:
        print('The numbers are equal.')
elif num_n % 10 > num_m % 10:
    print(num_n)
elif num_m % 10 > num_n % 10:
    print(num_m)
