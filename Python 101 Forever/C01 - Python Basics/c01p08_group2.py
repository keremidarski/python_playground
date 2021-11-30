# Problem description:
# https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/19-C01P08

def group(items):
    result = []
    length = len(items)
    index = 0

    while index < length:
        item = items[index]
        temp_group = [item]

        next_index = index + 1

        while next_index < length and items[next_index] == item:
            temp_group.append(items[next_index])
            next_index += 1

        result.append(temp_group)
        index = next_index
        
    return result

tests = [group([1, 1, 1, 2, 3, 1, 1]) == [[1, 1, 1], [2], [3], [1, 1]],
        group([1, 2, 1, 2, 3, 3]) == [[1], [2], [1], [2], [3, 3]],
        group([]) == [],
        group([1]) == [[1]],
        group([1, 1, 1, 1]) == [[1, 1, 1, 1]]]

# Expected: True
for test in tests:
    print(test)
