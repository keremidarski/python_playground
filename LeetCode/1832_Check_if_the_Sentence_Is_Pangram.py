def is_pangram(sentence):
    return 26 == len(set(list(sentence)))

print(is_pangram('thequickbrownfoxjumpsoverthelazydog'))
