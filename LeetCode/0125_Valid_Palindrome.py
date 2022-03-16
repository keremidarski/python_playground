# Problem description:
# https://leetcode.com/problems/valid-palindrome/


def is_palindrome(s):
    new_s = ''.join(char for char in s.lower() if char.isalnum())
    
    return new_s == new_s[::-1]
