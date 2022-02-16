# Problem description:
# https://leetcode.com/problems/roman-to-integer/

def roman_to_int(s):
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    result = 0

    for i in range(len(s) - 1):
        if roman[s[i]] < roman[s[i + 1]]:
            result -= roman[s[i]]
        else:
            result += roman[s[i]]

    return result + roman[s[-1]]

# Expected: 3
print(roman_to_int('III'))
