# Problem description:
# https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/19-C01P08

def group(items):
    result = []
    temp_group = []

    if len(items) < 1:
        return result

    for item in items:
        if len(temp_group) == 0:
            temp_group.append(item)
        elif item in temp_group:
            temp_group.append(item)
        else:
            result.append(temp_group)
            temp_group = [item]
    
    result.append(temp_group)
    
    return result

tests = [group([1, 1, 1, 2, 3, 1, 1]) == [[1, 1, 1], [2], [3], [1, 1]],
        group([1, 2, 1, 2, 3, 3]) == [[1], [2], [1], [2], [3, 3]],
        group([]) == [],
        group([1]) == [[1]],
        group([1, 1, 1, 1]) == [[1, 1, 1, 1]]]

# Expected: True
for test in tests:
    print(test)
