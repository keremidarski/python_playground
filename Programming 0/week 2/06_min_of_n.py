# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week2/2-List-Problems

n = int(input('Enter n: '))

counter = 0
numbers = []

while counter < n:
    number = int(input())
    numbers += [number]
    counter += 1

current_min = numbers[0]

for i in numbers:
    if i < current_min:
        current_min = i

print(f'Max is: {current_min}')
