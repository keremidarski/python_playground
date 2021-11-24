def is_palindrome(number):
    non_reversed = number
    reversed_number = 0

    while number != 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10
    return non_reversed == reversed_number

def palindromes_count(number):
    result = 0

    for n in range(10, number + 1):
        if is_palindrome(n):
            result += 1

    return result

tests = [
    (10, 0),
    (20, 1),
    (30, 2),
    (101, 10),
    (200, 19),
    (43539, 525),
    (4247, 132),
    (48877, 577),
    (94012, 1029),
    (62560, 715),
    (92009, 1009),
    (63176, 721),
    (67409, 763),
    (62834, 718),
    (77420, 863),
    (99999, 1089),
]

for n, expected in tests:
    result = palindromes_count(n)

    print(result == expected)