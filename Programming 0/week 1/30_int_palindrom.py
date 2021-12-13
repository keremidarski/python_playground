number = int(input('Enter number: '))

non_reversed = number
reversed_number = 0

while number != 0:
    digit = number % 10

    reversed_number = reversed_number * 10 + digit

    number = number // 10

if non_reversed == reversed_number:
    print(str(non_reversed) + " is a palindrom")
else:
    print(str(non_reversed) + " is not a palindrom")