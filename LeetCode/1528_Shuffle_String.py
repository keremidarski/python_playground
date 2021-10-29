# https://leetcode.com/problems/shuffle-string/

# Given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
# Return the shuffled string.

def restore_string(str, indices):
    result = indices.copy()
    str_list = list(str)
        
    for index, value in enumerate(indices):
        result[value] = str_list[index]
            
    return ''.join(result)

# Expected: "arigatou"
print(restore_string("aaiougrt", [4, 0, 2, 6, 7, 3, 1, 5]))
