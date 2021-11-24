from enum import Enum

class Monotonicity(Enum):
    INCREASING = 1
    DECREASING = 2
    NONE = 3

def increasing_or_decreasing(ns):
    is_incr = False
    is_decr = False

    for i in range(len(ns) - 1):
        if ns[i] < ns[i + 1]:
            is_incr = True
        elif ns[i] > ns[i + 1]:
            is_decr = True
        elif ns[i] == ns[i + 1]:
            return Monotonicity.NONE
    if is_incr == True and is_decr == False:
        return Monotonicity.INCREASING
    elif is_incr == False and is_decr == True:
        return Monotonicity.DECREASING
    else:
        return Monotonicity.NONE

print(increasing_or_decreasing([1, 2, 3, 4, 5]) == Monotonicity.INCREASING)
print(increasing_or_decreasing([5, 6, -10]) == Monotonicity.NONE)
print(increasing_or_decreasing([1, 1, 1, 1]) == Monotonicity.NONE)
print(increasing_or_decreasing([9, 8, 7, 6]) == Monotonicity.DECREASING)
print(increasing_or_decreasing([]) == Monotonicity.NONE)
print(increasing_or_decreasing([1]) == Monotonicity.NONE)
print(increasing_or_decreasing([1, 100]) == Monotonicity.INCREASING)
print(increasing_or_decreasing([1, 100, 100]) == Monotonicity.NONE)
print(increasing_or_decreasing([100, 1]) == Monotonicity.DECREASING)
print(increasing_or_decreasing([100, 1, 1]) == Monotonicity.NONE)
print(increasing_or_decreasing([100, 1, 2]) == Monotonicity.NONE)