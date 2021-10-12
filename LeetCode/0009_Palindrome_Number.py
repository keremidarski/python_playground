def is_palindrome(x):
    result = []
    
    for i in str(x):
        result.insert(0, str(i))

    if str(x) == ''.join(result):
        return True
    else:
        return False

print(is_palindrome(12321))