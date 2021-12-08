# Problem description:
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

def kids_with_candies(candies, extraCandies):
    result = []
    max_candy = candies.copy()
    max_candy.sort()
    max_candy = max_candy[-1]

    for kid in candies:
        if kid + extraCandies >= max_candy:
            result.append(True)
        else:
            result.append(False)

    return result

# Expected: [true, false, false, false, false]
print(kids_with_candies([4, 2, 1, 1, 2], 1))
