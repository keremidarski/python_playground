# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week2/4-Three-More-Problems

string = input('Enter text: ')

counter = 0
vowels = "aeiouyAEIOUY"

for ch in string:
    if ch in vowels:
        counter += 1

print(counter)
