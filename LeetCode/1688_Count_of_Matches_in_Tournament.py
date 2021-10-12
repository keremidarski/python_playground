def number_of_matches(n):
    result = 0

    while n > 1:
        if n % 2 == 1:
            n -= 1
            result += 1
        n -= n // 2
        result += n 

    return result

print(number_of_matches(14))