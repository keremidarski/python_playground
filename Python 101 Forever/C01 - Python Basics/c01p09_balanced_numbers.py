# Problem description:
# https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/20-C01P09

def is_number_balanced(number):
    number = str(abs(number))
    half = len(number) // 2
    left = []
    right = []
    
    for n in range(half):
        left.append(int(number[n]))
        right.append(int(number[-(n + 1)]))
    
    return sum(left) == sum(right)

tests = [is_number_balanced(9) is True,
        is_number_balanced(4518) is True,
        is_number_balanced(28471) is False,
        is_number_balanced(1238033) is True]

# Expected: True
for test in tests:
    print(test)
