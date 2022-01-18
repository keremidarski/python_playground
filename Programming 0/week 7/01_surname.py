# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week7/1-Taken-Name

def taken_name(surname_husband, surname_wife):
    if surname_husband in surname_wife:
        return True
    else:
        return False

print(taken_name('Petrov', 'Ivanova-Petrova'))
