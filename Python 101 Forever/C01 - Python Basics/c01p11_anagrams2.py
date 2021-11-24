def char_histogram(string):
    string = string.lower().replace(' ', '')
    result = {}

    for char in string:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1
    return result

def anagrams(word1, word2):
    return char_histogram(word1) == char_histogram(word2)

tests = [
        anagrams("listen", "silent") is True,
        anagrams("LISTEN", "silent") is True,
        anagrams("python", "ruby") is False,
        anagrams("New York Times", "monkeys write") is True,
        anagrams("snake", "sssnakee") is False
        ]

for test in tests:
    print(test)