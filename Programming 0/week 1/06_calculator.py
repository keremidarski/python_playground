# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week1/2-If-Elif-Else-Simple-Problems

num_a = int(input('Enter a: '))
num_b = int(input('Enter b: '))
oper = input('Enter operation: ')

if oper == '+':
    print(f'Result is: {num_a + num_b}')
elif oper == '-':
    print(f'Result is: {num_a - num_b}')
elif oper == '*':
    print(f'Result is: {num_a * num_b}')
elif oper == '/':
    print(f'Result is: {num_a / num_b}')
else:
    print('We do not support that operation.')
