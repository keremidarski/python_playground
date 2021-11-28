# Problem description:
# https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/16-C01P05

def sum_matrix(m):
    result = 0

    for l in m:
        for n in l:
            result += n

    return result

# Expected: 55
print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))
