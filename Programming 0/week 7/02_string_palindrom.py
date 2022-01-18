# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week7/2-Coolest-Palindrome

def is_palindrom(string):
    string = string.lower()
    normal = []
    reversed = []

    for letter in string:
        if letter != ' ' and letter != ',' and letter != '.' and letter != '!' and letter != '?':
            normal.append(letter)
    
    reversed = normal.copy()
    reversed.reverse()

    if normal == reversed:
        return True
    else:
        return False

print(is_palindrom('Az obi4am ma4 i boza!!!'))
