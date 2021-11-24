def word_counter(matrix, word):
    result = 0
    left_to_right = list(word)
    right_to_left = list(reversed(word))
    length = len(word)

    for row in matrix:
        for i in range(len(row) - (length - 1)):
            horizontal_sequence = []

            for j in range(length):
                horizontal_sequence.append(row[i + j])

            if horizontal_sequence == left_to_right or horizontal_sequence == right_to_left:
                result += 1

    for column in range(len(matrix) - (length - 1)):
        for i in range(len(matrix[0])):
            vertical_sequence = []

            for j in range(length):
                vertical_sequence.append(matrix[j + column][i])

            if vertical_sequence == left_to_right or vertical_sequence == right_to_left:
                result += 1

    row_counter = 0
    column_counter = 0
    for i in range(len(matrix) - (length - 1)):
        for j in range(len(matrix[0]) - (length - 1)):
            right_diagonal_sequence = []
            row = 0
            column = 0

            while column < length:
                right_diagonal_sequence.append(matrix[row + row_counter][column + column_counter])
                row += 1
                column += 1

            if right_diagonal_sequence == left_to_right or right_diagonal_sequence == right_to_left:
                result += 1
            
            column_counter += 1
        row_counter += 1
        column_counter = 0

    row_counter = 0
    column_counter = 0
    for i in range(len(matrix) - (length - 1)):
        for j in range(len(matrix[0]) - (length - 1)):
            left_diagonal_sequence = []
            row = 0
            column = (len(matrix)) - (length - 1)

            while column >= 0:
                left_diagonal_sequence.append(matrix[row + row_counter][column + column_counter])
                row += 1
                column -= 1

            if left_diagonal_sequence == left_to_right or left_diagonal_sequence == right_to_left:
                result += 1
            
            column_counter += 1
        row_counter += 1
        column_counter = 0

    return result

word = "ivan"
matrix = [
    ["i", "v", "a", "n"],
    ["e", "v", "n", "h"],
    ["i", "n", "a", "v"],
    ["m", "v", "v", "n"],
    ["q", "r", "i", "t"]
]
print(word_counter(matrix, word))