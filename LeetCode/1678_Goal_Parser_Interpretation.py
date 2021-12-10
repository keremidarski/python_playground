# Problem description:
# https://leetcode.com/problems/goal-parser-interpretation/

def interpret(command):
    return command.replace('()', 'o').replace('(al)', 'al')

# Expected: 'Gooooal'
print(interpret('G()()()()(al)'))
