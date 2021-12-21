# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week2/2-List-Problems

n = int(input("Enter count of numbers: "))

count = 1
numbers = []

while count <= n:
    number = int(input("Enter number: "))
    numbers = numbers + [number]
    count += 1

print(numbers)
