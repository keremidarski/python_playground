def matrix_dimensions(matr):
    row_count = len(matr)
    column_count = len(matr[0])

    return f'The matrix has dimensions: {row_count}x{column_count}'

def matrix_sum(matr):
    total_sum = 0

    n = len(matr)
    m = len(matr[0])

    for row_index in range(0, n):
        for column_index in range(0, m):
            element = matr[row_index][column_index]
            total_sum += element
    return total_sum

a = [ [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9] ]

print(matrix_dimensions(a))
print(matrix_sum(a))