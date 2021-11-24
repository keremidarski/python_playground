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

print(iban_formatter2("BG80BNBG96611020345678"))