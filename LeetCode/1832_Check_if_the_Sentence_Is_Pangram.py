# Problem description:
# https://leetcode.com/problems/check-if-the-sentence-is-pangram/

def is_pangram(sentence):
    return 26 == len(set(list(sentence)))

# Expected: True
print(is_pangram('thequickbrownfoxjumpsoverthelazydog'))
