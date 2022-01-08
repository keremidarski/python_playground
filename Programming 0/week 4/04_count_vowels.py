# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week4/4-Count-Vowels-Consonants

def count_vowels_consonants(word):
    result = {'vowels': 0, 'consonants': 0}

    for letter in word:
        if letter in 'aeiouyAEIOUY':
            result['vowels'] += 1
        else:
            result['consonants'] += 1
    return result

print(count_vowels_consonants("aaAFcccD"))
