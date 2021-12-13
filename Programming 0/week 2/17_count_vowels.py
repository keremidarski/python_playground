string = input('Enter text: ')

counter = 0
vowels = "aeiouyAEIOUY"

for ch in string:
    if ch in vowels:
        counter += 1

print(counter)