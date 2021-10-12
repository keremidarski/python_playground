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

print(kids_with_candies([4,2,1,1,2], 1))