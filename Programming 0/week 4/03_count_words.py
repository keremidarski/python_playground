# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week4/3-Count-Words

def count_words(words):
    result = {}
    
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result

# Expected: {'words': 3, 'are': 2, 'meaningful': 1}
print(count_words(['words', 'are', 'meaningful', 'words', 'words', 'are']))
