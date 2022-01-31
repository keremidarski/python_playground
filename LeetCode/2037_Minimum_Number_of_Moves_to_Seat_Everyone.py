# Problem description:
# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

def min_moves_to_seat(seats, students):
    result = 0
    sorted_seats = sorted(seats)
    sorted_students = sorted(students)

    for i in range(len(sorted_students)):
        result += abs(sorted_students[i] - sorted_seats[i])

    return result