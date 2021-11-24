# Problem description:
# https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/12-C01P01

def iban_formatter(iban):
    iban = iban.replace(' ', '')
    i_list = []
    count = 0
    index = 0
    group = ''

    for i in range(6):
        while count < 4:
            if index < len(iban):
                group += iban[index]
                count += 1
                index += 1
            else:
                break
        i_list.append(group)
        group = ''
        count = 0

    result = ' '.join(i_list)

    return result

print(iban_formatter("BG80 BNBG 9661 1020 3456 78"))
