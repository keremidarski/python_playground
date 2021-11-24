def char_histogram(string):
    result = {}

    for char in string:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1

    return result

print(char_histogram("Python!"))