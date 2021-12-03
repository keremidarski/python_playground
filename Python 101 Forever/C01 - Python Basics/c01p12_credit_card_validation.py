# Problem description:
# https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/23-C01P12

def is_credit_card_valid(number):
    n_list = list(str(number))
    result = []

    for index in range(1, len(n_list) + 1):
        digit_sum = int(n_list[-index]) * 2
        if index % 2 == 0:
            if digit_sum > 9:
                a = digit_sum % 10
                b = digit_sum // 10
                result.insert(0, a + b)
            else:
                result.insert(0, digit_sum)
        else:
            result.insert(0, int(n_list[-index]))
    ''.join(str(result))
    return sum(result) % 10 == 0

tests = [
    (79927398713, True),
    (4417123456789113, True),
    (4242424242424242, True),
    (79927398715, False),
    (79927398710, False),
    (79927398711, False),
    (79927398712, False),
    (79927398714, False),
    (79927398715, False),
    (79927398716, False),
    (79927398717, False),
    (79927398718, False),
    (79927398719, False)
]


for number, expected in tests:
    result = is_credit_card_valid(number)
    
    # Expected: True
    print(result == expected)
