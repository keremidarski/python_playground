# https://leetcode.com/problems/reverse-prefix-of-word/

# Given a 0-indexed string word and a character ch, reverse the segment of word
# that starts at index 0 and ends at the index of the first occurrence of ch (inclusive).
# If the character ch does not exist in word, do nothing.
# For example, if word = "abcdefd" and ch = "d", then you should reverse the segment
# that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
# Return the resulting string.

def reverse_prefix(word, ch):
    prefix = []
    counter = 0
    
    for char in word:
        if char != ch:
            prefix.append(char)
        else:
            prefix.append(char)
            counter += 1

            if counter == 1:
                prefix.reverse()

    return ''.join(prefix)

print(reverse_prefix('abcdefd', 'd'))