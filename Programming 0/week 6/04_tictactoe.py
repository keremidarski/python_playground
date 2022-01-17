# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week6/4-Print-Tic-Tac-Toe

def board_to_string(board):
    row_one = board[0]
    row_two = board[1]
    row_three = board[2]

    return f'| {row_one[0]} | {row_one[1]} | {row_one[2]} |\n| {row_two[0]} | {row_two[1]} | {row_two[2]} |\n| {row_three[0]} | {row_three[1]} | {row_three[2]} |'


board = [ ["X", "O", "#"],
          ["X", "X", "X"],
          ["#", "#", "#"] ]

print(board_to_string(board))
