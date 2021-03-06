# Problem description:
# https://leetcode.com/problems/is-subsequence/

def is_subsequence(s, t):
    i, j = 0, 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    
    return True if i == len(s) else False


# Expected: True
print(is_subsequence('abc', 'ahbgdc'))
# Expected: False
print(is_subsequence('axc', 'ahbgdc'))
# Expected: False
print(is_subsequence('ace', 'aec'))
