def count_zero_neighbours(numbers):
    counter = 0
    length = len(numbers)

    for index_x in range(0, length):
        for index_y in range(index_x + 1, length):
            x = numbers[index_x]
            y = numbers[index_y]

            if x + y == 0:
                counter += 1
    return counter

print(count_zero_neighbours([1, -1, 2, -2, 0, 0, 5, -5]))
