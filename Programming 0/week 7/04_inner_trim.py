def trim(string):
    first_trim = ''
    second_trim = ''
    end_counter = 0

    for i in range(0, len(string)):
        if string[i].startswith(' ') == False:
            for index in range(i, len(string)):
                first_trim += str(string[index])
            break
    for i in range(1, len(first_trim)): 
        if first_trim[-i].endswith(' ') == True:
            end_counter += 1
        else:
            for index in range(0, len(first_trim) - end_counter):
                second_trim += str(first_trim[index])
            break
            
    return second_trim

def inner_trim(string):
    trimmed = trim(string)
    result = []

    for word in trimmed.split(' '):
        if word == '':
            continue
        else:
            result.append(word)

    return ' '.join(result)

# Expected: 'edno dve tri'
print(inner_trim('     edno     dve    tri   '))
