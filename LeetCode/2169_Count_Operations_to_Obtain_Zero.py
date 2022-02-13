# Problem description:
# https://leetcode.com/problems/count-operations-to-obtain-zero/

def count_operations(num1, num2):
    operations = 0

    while num1 > 0 and num2 > 0:
        if num1 >= num2:
            num1 -= num2
            operations += 1
        else:
            num2 -= num1
            operations += 1

    return operations

print(count_operations(2, 3))
