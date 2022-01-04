# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week4/2-Hash-Them

def hash_them(keys, values):
    result = {}
    
    index = 0

    for key in keys:
        if index < len(values):
            result[key] = values[index]
        else:
            result[key] = None

        index += 1

    return result

print(hash_them(['Ivan', 'Maria'], [1, 2]))
