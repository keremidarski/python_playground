# Problem description:
# https://leetcode.com/problems/valid-anagram/

def is_anagram(s, t):
    s_occurances = {}
    t_occurances = {}
        
    for char in s:
        if char not in s_occurances:
            s_occurances[char] = 1
        else:
            s_occurances[char] += 1
            
    for char in t:
        if char not in t_occurances:
            t_occurances[char] = 1
        else:
            t_occurances[char] += 1
            
    return s_occurances == t_occurances


# Expected: True
print(is_anagram("anagram", "nagaram"))
# Expected: False
print(is_anagram("rat", "car"))
