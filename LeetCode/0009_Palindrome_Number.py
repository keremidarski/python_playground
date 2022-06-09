# Problem description:
# https://leetcode.com/problems/palindrome-number/


def is_palindrome(x):
    result = []
    
    for i in str(x):
        result.insert(0, str(i))

    if str(x) == ''.join(result):
        return True
    
    return False


# Expected: True
print(is_palindrome(121))
# Expected: False
print(is_palindrome(1231))
# Expected: False
print(is_palindrome(-121))
