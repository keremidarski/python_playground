# https://leetcode.com/problems/palindrome-number/

# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

def is_palindrome(x):
    result = []
    
    for i in str(x):
        result.insert(0, str(i))

    if str(x) == ''.join(result):
        return True
    else:
        return False

# Expected: True
print(is_palindrome(121))
# Expected: False
print(is_palindrome(1231))
# Expected: False
print(is_palindrome(-121))
