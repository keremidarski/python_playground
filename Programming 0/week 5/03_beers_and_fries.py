# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week5/3-Beer-and-Fries

def max_score(beers, fries):
    beers.sort(reverse = True)
    fries.sort(reverse = True)
    max_score = 0

    for i in range(0, len(beers)):
        max_score += beers[i] * fries[i]

    return max_score

print(max_score([10, 11], [1, 5]))
