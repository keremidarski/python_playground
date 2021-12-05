# Problem description:
# https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/29-C01P18

import copy

def out_of_bounds(point, matrix):
    x, y = point

    MIN_X = 0
    MAX_X = len(matrix) - 1
    MIN_Y = 0
    MAX_Y = len(matrix[0]) - 1

    return x < MIN_X or x > MAX_X or y < MIN_Y or y > MAX_Y

def matrix_bombing_plan(m):
    result = {}

    for row_index in range(len(m)):
        for column_index in range(len(m[0])):
            matrix = copy.deepcopy(m)
            position = row_index, column_index
            matrix_sum = 0

            for temp_row in range(row_index - 1, row_index + 2):
                for temp_column in range(column_index - 1, column_index + 2):
                    temp_position = temp_row, temp_column

                    if out_of_bounds(temp_position, matrix):
                        continue

                    if temp_position == position:
                        continue

                    if matrix[temp_row][temp_column] - matrix[row_index][column_index] < 0:
                        matrix[temp_row][temp_column] = 0
                    else:
                        matrix[temp_row][temp_column] -= matrix[row_index][column_index]

            matrix_sum += sum(sum(row) for row in matrix)          
            result[position] = matrix_sum

    return result

m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

# Expected: {(0, 0): 42,
#  (0, 1): 36,
#  (0, 2): 37,
#  (1, 0): 30,
#  (1, 1): 15,
#  (1, 2): 23,
#  (2, 0): 29,
#  (2, 1): 15,
#  (2, 2): 26}
print(matrix_bombing_plan(m))
