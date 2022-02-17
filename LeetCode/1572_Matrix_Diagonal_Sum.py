# Problem description:
# https://leetcode.com/problems/roman-to-integer/

def diagonal_sum(mat):
    result = {}
    column = 0

    for i in range(len(mat)):
        position = i, i
        result[position] = result.get(position, mat[i][i])

    for i in range(len(mat) - 1, - 1, - 1):
        position = i, column
        result[position] = result.get(position, mat[i][column])
        column += 1

    return sum(result.values())


mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
print(diagonal_sum(mat))
