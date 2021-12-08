# Problem description:
# https://leetcode.com/problems/maximum-69-number/

def maximum_69_number(num):
    digits = list(str(num))
    
    for index, digit in enumerate(digits):
        if digit != '9':
            digits[index] = '9'
            break

    return int(''.join(digits))

# Expected: 9969
print(maximum_69_number(9669))
