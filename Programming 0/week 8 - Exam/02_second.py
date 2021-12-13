def second_largest(numbers):
    numbers.sort()
    largest_num = numbers[-1]
    same_number = False

    if len(numbers) < 2:
        return False
    for num in numbers:
        if num == largest_num:
            same_number = True
        else:
            same_number = False
    if same_number:
        return False

    for num in range(len(numbers), 0, -1):
        if numbers[num - 1] != largest_num:
            return numbers[num - 1]

print(second_largest([5, 5]))