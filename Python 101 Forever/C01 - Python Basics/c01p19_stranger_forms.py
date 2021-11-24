from copy import deepcopy
from pprint import pprint

def out_of_bounds(point, matrix):
    x, y = point

    MIN_X = 0
    MAX_X = len(matrix) - 1
    MIN_Y = 0
    MAX_Y = len(matrix[0]) - 1

    return x < MIN_X or x > MAX_X or y < MIN_Y or y > MAX_Y


def get_seats(row_index, column_index, friends_configuration):
    result = []
    
    for friend in friends_configuration:
        person = []

        if len(friend) == 1:
            person = [friend, row_index, column_index]
            result.append(person)
            continue
        else:
            name = friend[0]
            direction = friend[1]
            target = friend[2]
                    
        if direction == 'A':
            for i in range(0, len(result)):
                if target == result[i][0]:
                    row = result[i][1] - 1
                    column = result[i][2]
                    person = [name, row, column]
                    result.append(person)
        elif direction == 'L':
            for i in range(0, len(result)):
                if target == result[i][0]:
                    row = result[i][1]
                    column = result[i][2] - 1
                    person = [name, row, column]
                    result.append(person)
        elif direction == 'R':
            for i in range(0, len(result)):
                if target == result[i][0]:
                    row = result[i][1]
                    column = result[i][2] + 1
                    person = [name, row, column]
                    result.append(person)
    
    return result


def stranger_forms(cinema_layout, friends_configuration):
    result = []

    for row_index in range(len(cinema_layout)):
        for column_index in range(len(cinema_layout[0])):
            layout = deepcopy(cinema_layout)
            does_fit = True

            if layout[row_index][column_index] == '.':
                seats = get_seats(row_index, column_index, friends_configuration)

                for seat in seats:
                    name = seat[0]
                    row = seat[1]
                    column = seat[2]

                    if not out_of_bounds((row, column), layout) and layout[row][column] == '.':
                        temp_list = list(layout[row])
                        temp_list[column] = name
                        layout[row] = ''.join(temp_list)
                    else:
                        does_fit = False
                        break
            else:
                continue

            if does_fit:
                result.append(layout)  
            
    return result


cinema_layout = ['..*...*.**',
                 '.....**...',
                 '*.*...*..*',
                 '.**....*.*',
                 '...*..*.*.',
                 '.***...*..',
                 '*......*.*',
                 '.....**..*',
                 '..*.*.*..*',
                 '***.*.**..']

friends_configuration = ["A", "BAA", "FRA", "CAB", "DRC", "EAD", "GLE"]

pprint(stranger_forms(cinema_layout, friends_configuration))