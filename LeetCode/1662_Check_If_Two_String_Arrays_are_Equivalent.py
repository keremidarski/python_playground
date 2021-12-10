# Problem description:
# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

def array_strings_are_equal(word1, word2):
    return ''.join(word1) == ''.join(word2)

# Expected: True
print(array_strings_are_equal(['ab', 'c'], ['a', 'bc']))
