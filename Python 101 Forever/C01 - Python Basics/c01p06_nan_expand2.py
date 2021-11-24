def nan_expand(times):
    result = ''

    if times == 0:
        return result

    result = ['Not a'] * times
    result.append('NaN')

    return ' '.join(result)

print(nan_expand(0))