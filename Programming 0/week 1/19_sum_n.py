# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week1/4-While-Loop-Problems

number = int(input('Enter number: '))
counter = 1
sum = 0

while counter <= number:
    sum += counter
    counter += 1

print(sum)
