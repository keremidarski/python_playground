# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week1/5-Saturday-Tasks

number = int(input('Enter number: '))

counter = 1
sum = 0

while counter <= number:
    if counter % 2 == 0:
        sum += counter
    counter += 1

print(sum)
