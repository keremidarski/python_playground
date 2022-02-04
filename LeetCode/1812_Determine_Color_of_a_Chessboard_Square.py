# Problem description:
# https://leetcode.com/problems/determine-color-of-a-chessboard-square/

def square_is_white(coordinates):
    row = int(coordinates[1])
    column = ord(coordinates[0]) - 96

    return (row + column) % 2 != 0

# Expected: True
print(square_is_white('h3'))
# Expected: False
print(square_is_white('a1'))