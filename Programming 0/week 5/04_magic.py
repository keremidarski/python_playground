# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week5/4-Magic-Square

def magic_square(square):
    is_magic = False
    square_sum = sum(square[0])
    row_one = sum(square[0])
    row_two = sum(square[1])
    row_three = sum(square[2])
    column_one = sum([square[0][0], square[1][0], square[2][0]])
    column_two = sum([square[0][1], square[1][1], square[2][1]])
    column_three = sum([square[0][2], square[1][2], square[2][2]])
    diagonal_one = sum([square[0][0], square[1][1], square[2][2]])
    diagonal_two = sum([square[0][2], square[1][1], square[2][0]])

    if (row_one + row_two + row_three + column_one + column_two + column_three + diagonal_one + diagonal_two) / 8 == square_sum:
        is_magic = True
        
    return is_magic

square = [ [23, 28, 21],
           [22, 24, 26],
           [27, 20, 25] ]

print(magic_square(square))
