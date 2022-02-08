# Problem description:
# https://leetcode.com/problems/robot-return-to-origin/

def judge_circle(moves):
    start_position = (0, 0)
    current_row = 0
    current_column = 0

    for move in moves:
        if move == 'U':
            current_row += 1
        elif move == 'D':
            current_row -= 1
        elif move == 'R':
            current_column += 1
        elif move == 'L':
            current_column -= 1

    return start_position == (current_row, current_column)

# Expected: True
print(judge_circle('UD'))
# Expected: False
print(judge_circle('LL'))
