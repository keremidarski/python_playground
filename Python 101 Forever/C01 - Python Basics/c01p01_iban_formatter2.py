# Problem description:
# https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/12-C01P01

def iban_formatter2(iban):
    result = []
    counter = 1

    for char in iban:
        if char == ' ':
            continue
        
        result.append(char)
        
        if counter == 4:
            result.append(' ')
            counter = 0
        
        counter += 1
    return ''.join(result)

# Expected: 'BG80 BNBG 9661 1020 3456 78'
print(iban_formatter2('BG80BNBG96611020345678'))
