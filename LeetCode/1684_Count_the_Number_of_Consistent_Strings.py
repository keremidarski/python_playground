# Problem description:
# https://leetcode.com/problems/count-the-number-of-consistent-strings/

def count_consistent_strings(allowed, words):
    result = 0
    in_allowed = False

    for word in words:
        for char in word:
            if char in list(allowed):
                in_allowed = True
            else:
                in_allowed = False
                break
        if in_allowed:
            result += 1
            
    return result

# Expected: True
print(count_consistent_strings('ab', ['ad', 'bd', 'aaab', 'baa', 'badab']) == 2)
