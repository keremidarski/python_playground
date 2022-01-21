# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/exam/3-Cipher-Text

def decode_word(encrypted_word, cipher):
    decrypted_word = ''
    
    for letter in encrypted_word:
        for key, value in cipher.items():
            if letter == value:
                decrypted_word += key

    return decrypted_word

print(decode_word('rpf', {'m': 'p', 'o': 'r', 'g': 'f'}))
