# https://leetcode.com/problems/truncate-sentence/

# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
# Each of the words consists of only uppercase and lowercase English letters (no punctuation).
# For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
# You are given a sentence s and an integer k. You want to truncate s such that it contains only the first k words.
# Return s after truncating it.

def truncate_sentence(s, k):
    truncated = []
    counter = 0
    
    for char in s:
        if char == ' ':
            counter += 1
            if counter < k:
                truncated.append(char)
            else:
                break
        else:
            truncated.append(char)

    s = ''.join(truncated)
    
    return s

# Expected: 'Hello how are you'
print(truncate_sentence('Hello how are you Contestant', 4))
