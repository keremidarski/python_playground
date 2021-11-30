# Problem description:
# https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/18-C01P07

from enum import Enum

class Monotonicity(Enum):
    INCREASING = 1
    DECREASING = 2
    NONE = 3

def increasing_or_decreasing(ns):
    length = len(ns)

    if length <= 1:
        return Monotonicity.NONE

    increasing = True
    decreasing = True

    for index in range(length - 1):
        a = ns[index]
        b = ns[index + 1]
        increasing = increasing and a < b
        decreasing = decreasing and a > b

    if increasing:
        return Monotonicity.INCREASING

    if decreasing:
        return Monotonicity.DECREASING
        
    return Monotonicity.NONE

# Expected: True
print(increasing_or_decreasing([1, 2, 3, 4, 5]) == Monotonicity.INCREASING)
print(increasing_or_decreasing([9, 8, 7, 6]) == Monotonicity.DECREASING)
print(increasing_or_decreasing([100, 1, 2]) == Monotonicity.NONE)
