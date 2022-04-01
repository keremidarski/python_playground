# Problem description:
# https://leetcode.com/problems/reverse-string/


def reverse_string(s):
    l, r = 0, len(s) - 1

    while l < r:
        s[l], s[r] = s[r], s[l]
        l, r = l + 1, r - 1


# Expected: ['o','l','l','e','h']
s = ['h','e','l','l','o']
reverse_string(s)
print(s)
