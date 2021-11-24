def nan_expand(times):
    nan = 'NaN'
    not_a = 'Not a '
    result = ''

    if times > 0:
        result = f'{not_a * times}{nan}'
    
    return result

print(nan_expand(3))