# Problem description:
# https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/21-C01P11

def anagrams(word1, word2):
    word1 = word1.lower().replace(' ', '')
    word2 = word2.lower().replace(' ', '')
    
    return sorted(word1) == sorted(word2)

tests = [
        anagrams("listen", "silent") is True,
        anagrams("LISTEN", "silent") is True,
        anagrams("python", "ruby") is False,
        anagrams("New York Times", "monkeys write") is True,
        anagrams("snake", "sssnakee") is False
        ]

for test in tests:
    # Expected: True
    print(test)
