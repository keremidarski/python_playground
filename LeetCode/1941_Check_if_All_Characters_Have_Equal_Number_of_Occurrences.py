# Problem description:
# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

def are_occurances_equal(s):
    occurances = {}
    result = True

    for char in s:
        if char in occurances:
            occurances[char] += 1
        else:
            occurances[char] = 1
    
    test_value = list(occurances.values())[0]

    for value in occurances.values():
        if value != test_value:
            result = False
            break
    
    return result

# Expected: True
print(are_occurances_equal('abacb'))