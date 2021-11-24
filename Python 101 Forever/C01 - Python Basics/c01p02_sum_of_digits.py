def sum_of_digits(nums):
    result = 0

    for n in str(nums):
        if n == '-':
            continue
        result += int(n)

    return result

print(sum_of_digits(-10))