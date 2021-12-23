# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week2/2-List-Problems

word = input('Enter word: ')
n = int(input('Enter n: '))
start = 0
words = []
counter = 0

while start < n:
    current_word = input()
    words += [current_word]
    start += 1

for i in words:
    if word in i:
        counter += 1

print(f'{word} is found {counter} times.')
