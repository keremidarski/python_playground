# https://leetcode.com/problems/maximum-69-number/

# Given a positive integer num consisting only of digits 6 and 9. 
# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6). 

def maximum_69_number(num):
    digits = list(str(num))
    
    for index, digit in enumerate(digits):
        if digit != '9':
            digits[index] = '9'
            break

    return int(''.join(digits))

# Expected: 9969
print(maximum_69_number(9669))
