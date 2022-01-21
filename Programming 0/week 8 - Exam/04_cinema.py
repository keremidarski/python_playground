# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/exam/4-Cinema-Seats

from sys import maxsize

def least_populated_row(cinema):
    max_row = maxsize
    rows_with_least_zeros = 0

    for index, row in enumerate(cinema):
        counter = 0
        
        for seat in row:
            if seat == 0:
                counter += 1
                
        if counter < max_row and counter != 0:
            max_row = counter
            rows_with_least_zeros = index
    
    return rows_with_least_zeros


def order_of_seats(cinema):
    result = []

    for row in cinema:
        least_populated = least_populated_row(cinema)

        for index, seat in enumerate(cinema[least_populated]):
            if seat == 0:
                result.append((least_populated + 1, index + 1))
                cinema[least_populated][index] = 1
    
    return result


print(order_of_seats([ [1, 1, 1],
           [1, 0, 0],
           [1, 0, 0],
           [1, 1, 0] ]))
