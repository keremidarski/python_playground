# Problem description:
# https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/17-C01P06

def nan_expand(times):
    nan = 'NaN'
    not_a = 'Not a '
    result = ''

    if times > 0:
        result = f'{not_a * times}{nan}'
    
    return result

# Expected: 'Not a Not a Not a NaN'
print(nan_expand(3))
