# https://leetcode.com/problems/determine-if-string-halves-are-alike/

# You are given a string s of even length. Split this string into two halves of equal lengths,
# and let a be the first half and b be the second half. Two strings are alike if they have the same number of vowels
# ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.
# Return true if a and b are alike. Otherwise, return false.

def halves_are_alike(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    a = []
    b = []
    counter_a = 0
    counter_b = 0

    for i in range(len(s)):
        if i < (len(s) // 2):
            a.append(s[i])
        else:
            b.append(s[i])

    for char in a:
        if char in vowels:
            counter_a += 1
    for char in b:
        if char in vowels:
            counter_b += 1

    return counter_a == counter_b

# Expected: True
print(halves_are_alike('book'))