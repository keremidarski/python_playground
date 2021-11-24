def string_reverse(s):
    return ''.join(reversed(s))

def is_integer_palindrome(x):
    x = str(x)
    return x == string_reverse(x)

def build_cache():
    result = {}
    n = 99999

    for x in range(10, n + 1):
        result[x] = is_integer_palindrome(x)
    return result

CACHE = build_cache()

def palindromes_count(n):
    count = 0

    for x in range(10, n + 1):
        if CACHE[x]:
            count += 1
    return count