# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week1/5-Saturday-Tasks

number = int(input('Enter a 3-digit number: '))

z = number % 10
number = number // 10
y = number % 10
number = number // 10
x = number % 10
number = number // 10

largest = x

if y >= largest and y >= z:
    largest = y
elif z >= largest and z >= y:
    largest = z

smallest = x

if y <= smallest and y <= z:
    smallest = y
elif z <= smallest and z <= y:
    smallest = z

middle = z

if (largest == z and smallest == y) or (smallest == z and largest == y):
    middle = x
elif (largest == z and smallest == x) or (smallest == z and largest == x):
    middle = y

max_number = largest * 100 + middle * 10 + smallest
min_number = smallest * 100 + middle * 10 + largest

print(f"Max number with those digits is: {max_number}")
print(f"Min number with those digits is: {min_number}")
