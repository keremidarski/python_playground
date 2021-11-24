def number_to_digits(number):
    digits = []
    number = abs(number)

    str_digits = list(str(number))

    for str_digit in str_digits:
        digits.append(int(str_digit))

    return digits

def is_number_balanced(number):
    digits = number_to_digits(number)
    length = len(digits)
    middle = length // 2
    is_odd_length = length % 2 == 1

    left_sum = 0
    right_sum = 0

    for index, digit in enumerate(digits):
        if index < middle:
            left_sum += digit
        else:
            if index == middle and is_odd_length:
                continue
            right_sum += digit
    return left_sum == right_sum

tests = [is_number_balanced(9) is True,
        is_number_balanced(4518) is True,
        is_number_balanced(28471) is False,
        is_number_balanced(1238033) is True]

for test in tests:
    print(test)