# Problem description:
# https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/17-C01P06

def nan_expand(times):
    result = ''

    if times == 0:
        return result

    result = ['Not a'] * times
    result.append('NaN')

    return ' '.join(result)

# Expected: 'Not a NaN'
print(nan_expand(1))
