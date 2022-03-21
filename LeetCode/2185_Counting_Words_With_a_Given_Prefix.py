# Problem description:
# https://leetcode.com/problems/counting-words-with-a-given-prefix/


def prefix_count(words, pref):
    res = 0

    for word in words:
        if word.startswith(pref):
            res += 1

    return res
