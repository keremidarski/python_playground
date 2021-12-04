# Problem description:
# https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/27-C01P16

def numbers_to_message(pressed_sequence):
    result = []
    letters = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
    last_number = None
    caps = False
    letter = 0
    button = 0

    for n in pressed_sequence:
        if n == -1 and last_number != None:
            if caps:
                result.append(str(letters[button][letter]).upper())
            else:
                result.append(str(letters[button][letter]))
            letter = 0
            last_number = None
            continue
        elif n == -1 and last_number == None:
            continue

        if n == 1:
            caps = True
            continue    
            
        if n == 0:
            if last_number == None:
                result.append(' ')
                continue
            if caps:
                result.append(str(letters[button][letter]).upper())
            else:
                result.append(str(letters[button][letter]))
            result.append(' ')
            letter = 0
            last_number = None
            caps = False
            continue

        if last_number == None:
            last_number = n
            letter = 0
            continue

        button = last_number - 2

        if n == last_number:
            letter += 1
            if letter > len(letters[button]) - 1:
                letter -= len(letters[button])
        else:
            if caps:
                result.append(str(letters[button][letter]).upper())
            else:
                result.append(str(letters[button][letter]))
            letter = 0
            last_number = n
            button = last_number - 2
            caps = False
    
    if last_number != None:
        button = last_number - 2
        result.append(str(letters[button][letter]))

    return ''.join(result)

# Expected: 'abc'
print(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]))
