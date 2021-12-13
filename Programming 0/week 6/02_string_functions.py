def string_to_char_list(string):
    result = []

    for ch in string:
        result += [ch]

    return result

def char_list_to_string(char_list):
    result = ""

    for ch in char_list:
        result += ch

    return result

def change_string(index, ch, string):
    char_list = string_to_char_list(string)

    char_list[index] = ch

    return char_list_to_string(char_list)

def reverse(str):
    reversed = ''
    for i in str:
        reversed = i + reversed
    return reversed

def join(delimiter, items):
    result = ''
    counter = 0

    for item in items:
        counter += 1

        if counter < len(items):
            result = result + str(item) + str(delimiter)
        else:
            result = result + str(item)
    return result
    
def startswith(search, string):
    does_start = False

    for i in range(0, len(search)):
        if string[i] == search[i]:
            does_start = True
        else:
            does_start = False
            break
    return does_start

def endswith(search, string):
    does_start = False

    for i in range(1, len(search) + 1):
        if string[-i] == search[-i]:
            does_start = True
        else:
            does_start = False
            break
    return does_start

def trim(string):
    first_trim = ''
    second_trim = ''
    end_counter = 0

    for i in range(0, len(string)):
        if startswith(' ', string[i]) == False:
            for index in range(i, len(string)):
                first_trim += str(string[index])
            break
    for i in range(1, len(first_trim)): 
        if endswith(' ', first_trim[-i]) == True:
            end_counter += 1
        else:
            for index in range(0, len(first_trim) - end_counter):
                second_trim += str(first_trim[index])
            break
    return second_trim

print(trim('     edno dve tri   ')) # -> 'edno dve tri'