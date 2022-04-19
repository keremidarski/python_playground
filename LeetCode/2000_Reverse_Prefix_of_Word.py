# Problem description:
# https://leetcode.com/problems/reverse-prefix-of-word/

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

# Expected: 'dcbaefd'
print(reverse_prefix('abcdefd', 'd'))
# Expected: 'zxyxxe'
print(reverse_prefix('xyxzxe', 'z'))

