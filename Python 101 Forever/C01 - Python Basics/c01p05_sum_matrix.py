def sum_matrix(m):
    result = 0

    for l in m:
        for n in l:
            result += n

    return result

print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))