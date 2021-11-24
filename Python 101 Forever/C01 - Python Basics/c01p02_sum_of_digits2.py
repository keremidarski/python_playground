def sum_of_digits(nums):
    result = 0
    nums = abs(nums)

    while nums > 0:
        digit = nums % 10
        result += digit
        nums = nums // 10

    return result

print(sum_of_digits(123))