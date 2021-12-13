def string_matrix(matrix_width, strings):
    for string in strings:
        if len(string) == matrix_width:
            print('|', end='')
            for char in string:
                print(f' {char}', end=' |')
            print('\n')
        elif len(string) < matrix_width:
            counter = matrix_width
            print('|', end='')
            for char in string:
                print(f' {char}', end=' |')
                counter -= 1
            while counter > 0:
                print(f' X', end=' |')
                counter -= 1
            print('\n')
        elif len(string) > matrix_width:
            counter = matrix_width
            print('|', end='')
            for char in string:
                print(f' {char}', end=' |')
                counter -= 1
                if counter == 0:
                    break
            print('\n')

print(string_matrix(6,["python","gogo","perl","java","haskell","ruby0nRails"]))