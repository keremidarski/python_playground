# Problem description:
# https://leetcode.com/problems/valid-parentheses/


def is_valid(s):
    stack = []
    close_to_open = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in close_to_open:
            if stack and stack[-1] == close_to_open[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return True if not stack else False


# Expected: True
print(is_valid('()'))
# Expected: True
print(is_valid('()[]{}'))
# Expected: False
print(is_valid('(]'))
