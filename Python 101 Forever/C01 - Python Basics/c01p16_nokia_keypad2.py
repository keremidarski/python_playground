# Problem description:
# https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/27-C01P16

def message_to_numbers(message):
    sequence = []
    letters = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
    last_key = None
    key = 0
    times_pressed = 0
    
    for char in message:
        if char == ' ':
            sequence.append(0)
            continue

        if char != char.lower():
            sequence.append(1)

        for button in letters:
            if char.lower() in button:
                key = letters.index(button) + 2

                for index, letter in enumerate(button):
                    if letter == char.lower():
                        times_pressed = index + 1
        
        if last_key == None:
            for time in range(times_pressed):
                sequence.append(key)
            last_key = key
            continue

        if last_key == key:
            sequence.append(-1)

        for time in range(times_pressed):
            sequence.append(key)
        last_key = key

    return sequence

# Expected: [2, -1, 2, 2, -1, 2, 2, 2]
print(message_to_numbers('abc'))
